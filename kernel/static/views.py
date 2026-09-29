from django.shortcuts import render

# Create your views here.

# Manejo de request con metodo GET a la ruta principal
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')