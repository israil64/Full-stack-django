<!-- ** 1 step for Django project start -->

# Environment Setup

# for windows

# python -m venv .venv

# to activate the virtual environment

source .venv/bin/activate

# for windows

# .venv\Scripts\activate

<!-- ** 2 step for Django project  -->

-- command 👇

# django-admin startproject yourProjectName

# cd yourProjectName

<!-- ** Start a Django Server -->

-- run command

# python manage.py runserver

<!-- ** FULLl A GUIDE ON DJANGO MODELS -->

-- if you are using image field, we need to install Pillow library to use it.

# python -m pip install Pillow

-- we need add some settings to our settings.py file to use the image field.

# COPY THIS LINES 👇

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

-- Now, let’s configure our projects urls.py file to reflect media files.

# COPY THIS LINES 👇 48 TO 51

from django.conf import settings
from django.conf.urls.static import static

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) [adding at the last]

<!-- ** Adding data to the database -->

python manage.py makemigrations
python manage.py migrate

<!-- ** ADDING CSS and JAVASCRIPT IN DJANGO -->

# add this css file go to settings.py and add the following line 👇:

import os #at the top of settings.py

'DIRS': ['templates'], OR 'DIRS' :[os.path.join(BASE_DIR, 'YOURPROJECTNAME/templates')]

# below this add the following line

STATIC_URL = '/static/'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# ADD AT THE TOP OF THE FILE IN HTML:

{% load static %}

# ADD THIS SCRIPT IN THE HEAD TAG:

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/index.js' %}"></script>
<link rel="shortcut icon" type="image/x-icon" href="{% static 'img/favicon.ico' %}"/>

                <!--** WE WANT TO CREATE APPS IN DJANGO  -->

# COPY THIS COMMAND LINE 👇 :

python manage.py startapp 'YOURAPPNAME'

# AND : GO TO setting.py & ADD IT TO THE INSTALLED_APPS.
