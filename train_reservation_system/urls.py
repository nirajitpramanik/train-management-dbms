# train_reservation_system/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),  # Redirect empty path to login page
    path('login/', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('register/', include('reservation.urls')),
    path('registration-success/', include('reservation.urls')),
    path('home/', include('reservation.urls')),
    path('dashboard/', include('reservation.urls')),
]
