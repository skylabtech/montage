from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_us, name='about_us'),
    path('landing/', views.landing, name='landing'),
    path('success/', views.success, name='success'),  # email sent success.


]
