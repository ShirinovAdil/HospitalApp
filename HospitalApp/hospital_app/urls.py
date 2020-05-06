from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.homepage, name="homepage"),
    re_path(r'^doctors-appointment$', views.make_appointment, name="make_appointment"),
    re_path(r'^hospitals$', views.hospital_list, name="hospital_list"),
    re_path(r'^specialities$', views.speciality_list, name="speciality_list"),
    re_path(r'^about$', views.about, name="about"),
    re_path(r'^contact$', views.contact, name="contact"),
    path('details/<int:id>/', views.hospital_detail, name="hospital_detail"),
    re_path(r'^thank-you$', views.thank_you, name="thank_you"),
    re_path(r'^thank-you-for-contacting$', views.thank_you_contact, name="thank_you_contact"),
]
