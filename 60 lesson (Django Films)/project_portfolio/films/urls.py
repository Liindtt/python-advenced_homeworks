from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("filter/", views.filter_film, name="filter_film"),
    path("filter_form/", views.filter_form, name="filter_form"),
    path('<int:id>/', views.film_detail, name='film_detail'),
]

