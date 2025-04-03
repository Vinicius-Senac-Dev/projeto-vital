from django.urls import path
#Com o . informamos que a que queremos importa a views que está na raiz do app usuarios
from . import views

urlpatterns = [
    # É dessa forma que o django envia as informações do html para a views, views.cadastro .cadastro é nome da minha função
    # Tem que ser definido um nome para que o html consiga encontrar e enviar informações
    # Posso definir qualquer name, mas esse nome será utilizado pelo html para receber e enviar dados
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('', views.home, name='home'),
    path('sair/', views.sair, name='sair'),
]