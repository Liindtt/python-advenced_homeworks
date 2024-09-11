from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.search_posts, name="post-list"),
    path('<int:id>/', views.post_detail, name="post-detail"),
    path('category/<int:category_id>/', views.posts_by_category, name='posts-by-category')
]
