from django.urls import path
from . import views

urlpatterns = [
    # deficion de ruta para la pagina principal
    path("", views.home, name="home"),
]