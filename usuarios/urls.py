from django.urls import path
#Com o . informamos que a que queremos importa a views que está na raiz do app usuarios
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro")
]