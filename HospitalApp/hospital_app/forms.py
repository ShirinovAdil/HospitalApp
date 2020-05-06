from django import forms
from .models import Appointment, Feedback, Contact


class DateTimeInput(forms.DateTimeInput):
    input_type = "date"


class DoctorRegistrationForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = "__all__"
        widgets = {'birthdate': DateTimeInput(),
                   'registration_date': DateTimeInput(),
                   }


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(label='', max_length=250,
                                   widget=forms.Textarea(attrs={'placeholder': 'Feedback text',
                                                                'style': 'resize:none;width:100%;height:100px;'
                                                                }))

    class Meta:
        model = Feedback
        fields = ['text']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"