from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.computers_list, name='computers_list'),  # Головна сторінка зі списком ПК
    path('computer/<int:pk>/', views.computer_detail, name='computer_detail'),  # Перегляд одного запису ПК
    path('computer/new/', views.create_computer, name='create_computer'),  # Створення нового запису
    path('computer/<int:pk>/edit/', views.edit_computer, name='edit_computer'),  # Редагування існуючого запису
    path('computer/<int:pk>/delete/', views.delete_computer, name='delete_computer'),  # Видалення ПК з підтвердженням
    path('search/', views.search_computer, name='search_computer'),  # Пошук за полем
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

