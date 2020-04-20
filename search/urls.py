from django.conf.urls import url
from django.contrib import admin
from .views import (searcharticles)
from . import views

app_name='search'


urlpatterns = [
    url('^$', views.searcharticles, name='searcharticles')
]
