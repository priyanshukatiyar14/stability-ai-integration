# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('generate-images/', views.generate_images, name='generate_images'),
]
