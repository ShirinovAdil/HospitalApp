from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^login/$', views.sign_in, name='login'),
    re_path(r'^logout/$', views.log_out, name='logout'),
]