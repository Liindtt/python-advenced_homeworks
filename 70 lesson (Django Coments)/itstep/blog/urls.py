from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path('<int:post_id>/', views.post_detail, name="post-detail"),
    path('cards/', views.post_cards, name="post-list-cards"),
    path('contact/', views.contact_view, name='contact'),

    path('tag/create/', views.create_tag, name="tag-create"),
    path('tag/<int:pk>/update', views.edit_tag, name="edit-tag"),

    path('post/create/', views.create_post, name='post-create'),
    path('post/<int:pk>/update/', views.edit_post, name='post-edit'),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),

]
