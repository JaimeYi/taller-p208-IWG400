from django.urls import path

from . import views

urlpatterns = [
    # deficion de ruta para pagina de login
    path("", views.login, name="login"),
]