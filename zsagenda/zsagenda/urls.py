"""zsagenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from regform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'is-reg-open/',
        views.is_registration_open,
        name='is_registration_open'
    ),
    path(
        'registrace-ukoncena/',
        views.registration_closed,
        name='registration_closed'
    ),
    path(
        'registrace-dokoncena/',
        views.registration_done,
        name='registration_done'
    ),
    path('', views.display_form, name='display_form'),
]
