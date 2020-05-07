from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, ContactForm
from django.utils import timezone
from django.contrib import messages
from .models import Hospital, Feedback, Speciality
from .forms import FeedbackForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random
# Create your views here.


def email(name, surname, email, date, doctor):
    import datetime
    subject = 'Uganda Hospital Appointment'
    message = f"Thank you {name} {surname} for choosing us for your {doctor} appointment. "
    message += f"Doctor will be waiting for you on date of: {date} at {random.randrange(9, 18)}:{random.randrange(10,60)}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def homepage(request):
    return render(request, "index.html")


@login_required(redirect_field_name='login')
def make_appointment(request):
    """Renders form to make an appointment"""
    if request.method == "POST":
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            today = timezone.now()
            register_date = form.cleaned_data.get('registration_date')
            birthdate = form.cleaned_data.get('birthdate')
            if today > register_date:
                messages.add_message(request, messages.WARNING, "You can't choose past time as registration date")
                return render(request, "appointment.html", {"form": form, "rError": 1})
            elif today < birthdate:
                messages.add_message(request, messages.WARNING, "Choose a valid birth date")
                return render(request, "appointment.html", {"form": form, "bError": 1})
            form.save(commit=True)
            name = form.cleaned_data.get("name")
            surname = form.cleaned_data.get("surname")
            gmail = form.cleaned_data.get("email")
            registration_date = form.cleaned_data.get("registration_date")
            registration_date = registration_date.strftime("%Y-%m-%d")
            doctor = form.cleaned_data.get("doctor")
            # send mail - > without redis
            email(name, surname, gmail, registration_date, doctor)
            return render(request, 'thank-you.html')
        return render(request, "appointment.html", {"form": form})
    else:
        data = {
            "email": request.user.email,
        }
        form = DoctorRegistrationForm(initial=data)
        return render(request, "appointment.html", {"form": form})


def hospital_list(request):
    """List all available hospitals"""
    all_hospitals = Hospital.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_hospitals, 5)
    try:
        hospital_list = paginator.page(page)
    except PageNotAnInteger:
        hospital_list = paginator.page(1)
    except EmptyPage:
        hospital_list = paginator.page(paginator.num_pages)
    return render(request, "hospital-list.html", {"hospital_list": hospital_list})


def hospital_detail(request, id):
    """returns info about particular hospital"""
    hospital = Hospital.objects.get(pk=id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.hospital = hospital
            form.save()
            return redirect('hospital_detail', id=id)
        else:
            form = FeedbackForm()
            return render(request, 'hospital-details.html', {'form': form})
    else:
        feedbacks_list = Feedback.objects.filter(hospital=hospital)
        page = request.GET.get('page', 1)
        paginator = Paginator(feedbacks_list, 3)
        try:
            feedbacks = paginator.page(page)
        except PageNotAnInteger:
            feedbacks = paginator.page(1)
        except EmptyPage:
            feedbacks = paginator.page(paginator.num_pages)
        form = FeedbackForm()
        context = {
            'hospital': hospital,
            'feedbacks': feedbacks,
            'feedback_form': form
        }
    return render(request, 'hospital-details.html', context)


def thank_you(request):
    """post registration thank you page"""
    return render(request, 'thank-you.html')


def thank_you_contact(request):
    """post contact thank you page"""
    return render(request, 'thank-you-contact.html')


def speciality_list(request):
    """list of all specialities"""
    all_specialities = Speciality.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_specialities, 5)
    try:
        specialities = paginator.page(page)
    except PageNotAnInteger:
        specialities = paginator.page(1)
    except EmptyPage:
        specialities = paginator.page(paginator.num_pages)
    return render(request, 'speciality.html', {"specialities": specialities})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank-you-contact.html')
        else:
            form = ContactForm()
            return render(request, 'contact.html', {"form": form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {"form": form})


def about(request):
    """ about page"""
    return render(request, 'about.html')
