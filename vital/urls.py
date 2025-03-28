from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Indicando o caminho(url) para rota de usuários.
    path('usuarios/', include('usuarios.urls'))
]
