# kasir/urls.py
from django.urls import path
from .views import kasir_home

urlpatterns = [
    path('', kasir_home, name='kasir_home'),
    # Tautkan URL lain jika diperlukan
]
