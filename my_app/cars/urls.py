from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cars-home'),
    path('about/',views.about, name='cars-about'),
    path('contact/',views.contact, name='cars-contact'),
]