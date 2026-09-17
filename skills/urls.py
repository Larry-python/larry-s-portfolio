from django.urls import path
from . import views

urlpatterns = [
    path("services/", views.services, name="services"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("projects/", views.projects, name="projects"),
    path( "testimonials/leave/", views.leave_testimonial, name="leave_testimonial"),
    path("testimonials/success/", views.testimonial_success, name="testimonial_success")
]