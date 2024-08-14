from django.urls import path
from .views import about, contact, projects, home

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("projects/", projects, name="projects"),
]

