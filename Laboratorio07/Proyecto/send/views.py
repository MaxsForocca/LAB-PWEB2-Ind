from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    send_mail('Hola desde Mi Proyecto de Django',
    'Hola, este es un mensaje automatico.',
    'mforocca@unsa.edu.pe',
    ['retac43400@msback.com'],
    fail_silently=False)
    
    return render(request, 'index.html')