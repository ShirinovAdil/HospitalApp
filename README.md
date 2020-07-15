# HospitalApp
Hospital registration application
Project for the Modern Programming Language course

## Prerequisites

 You should have python 3.8 and Redis server up and running

## Installing

 Create python virtual environment and run:
 
     pip3 install -r requirements.txt

## Setup
   To make proper use of mailing system, set up email credentials in `settings.py`
     
    MY_EMAIL_HOST = "yourlogin"
    MY_EMAIL_PWD = "yourpass"
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = MY_EMAIL_HOST
    EMAIL_HOST_PASSWORD = MY_EMAIL_PWD
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    
## Make initial database migrations

     python3 manage.py check 

     python3 manage.py migrate 

## Run the server by writing:

    python3 manage.py runserver 
