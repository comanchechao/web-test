from django.conf.urls import url
from django.contrib import admin
from .views import (searcharticles)

urlpatterns = [
    url('^$', searcharticles, name='searcharticles')
]
