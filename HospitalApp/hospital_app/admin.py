from django.contrib import admin

from . models import *

admin.site.register(Hospital)
admin.site.register(Feedback)
admin.site.register(Appointment)
admin.site.register(Speciality)