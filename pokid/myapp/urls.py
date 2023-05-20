from django.contrib import admin
from django.urls import path, include
from .views import pokid_view

urlpatterns = [
    path('', pokid_view),
]