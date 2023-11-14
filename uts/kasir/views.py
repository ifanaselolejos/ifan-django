# views.py di aplikasi kasir
from django.shortcuts import render

def kasir_home(request):
    return render(request, 'kasir/home.html')

