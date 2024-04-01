from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .models import CustomLoginView

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL для реєстрації
    path('login/', CustomLoginView.as_view(), name='login'),  # URL для входу
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL для виходу
    path('profile/', views.profile, name='profile'),  # URL для перегляду профілю
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # URL для редагування профілю
]
