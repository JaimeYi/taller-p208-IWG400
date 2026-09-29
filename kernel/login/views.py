from django.shortcuts import render

# Create your views here.

# Manejo de request con metodo GET y POST en la pagina de login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
            return render(request, 'login.html', {"text": "Función pendiente de implementar"})