from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),  # URL для списку послуг
    path('add/', views.add_service, name='add_service'),  # URL для додавання нової послуги
    path('<int:service_id>/', views.service_detail, name='service_detail'),  # URL для деталей конкретної послуги
    path('<int:service_id>/edit/', views.edit_service, name='edit_service'),  # URL для редагування послуги
    path('<int:service_id>/delete/', views.delete_service, name='delete_service'),  # URL для видалення послуги
]
