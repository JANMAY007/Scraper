from django.urls import path
from .views import scraper

urlpatterns = [
    path('', scraper, name='scraper'),
]
