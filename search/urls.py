from django.conf.urls import url
from django.contrib import admin
from .views import (searcharticles)

app_name='search'


urlpatterns = [
    url('^$', searcharticles, name='searcharticles')
]
