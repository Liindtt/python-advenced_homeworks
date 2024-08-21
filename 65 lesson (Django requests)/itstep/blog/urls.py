from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path('<int:id>/', views.post_detail, name="post-detail"),
    path('cards/', views.post_cards, name="post-list-cards"),
    path('tag/<slug:slug>/', views.post_by_tag, name='post-by-tag')
]
