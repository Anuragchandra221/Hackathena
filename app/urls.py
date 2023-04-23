from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.question),
    path('next/', views.next_question),
]
