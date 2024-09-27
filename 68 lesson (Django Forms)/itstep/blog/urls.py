from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path('<int:id>/', views.post_detail, name="post-detail"),
    path('cards/', views.post_cards, name="post-list-cards"),
    path('tag/create/', views.create_tag, name="create-tag"),
    path('tag/update/<int:pk>', views.edit_tag, name="edit-tag"),
    path('tag/delete/<int:pk>', views.delete_tag, name="delete-tag"),
    path('rate/<int:post_id>/', views.rate_post, name='rate-post'),
]
