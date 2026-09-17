from django.urls import path
from .views import home, about_me, contact



urlpatterns = [
    path('', home, name= 'home'),
    path('about', about_me, name='about-me' ),
    path("contact/", contact, name="contact"),
]