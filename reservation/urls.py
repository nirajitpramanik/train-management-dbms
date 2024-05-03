# reservation/urls.py

from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Redirect empty path to login page
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
