from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("weather/<str:mul>", views.weather_bs4, name="weather_bs4"),
    path('currency/', views.currency_sel, name='exchange_rates'),
]
