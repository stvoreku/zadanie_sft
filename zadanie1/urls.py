from django.contrib import admin
from django.urls import path, include
from .views import PersonView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(PersonView.as_view())),
]
