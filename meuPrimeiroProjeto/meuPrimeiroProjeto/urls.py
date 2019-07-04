"""meuPrimeiroProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .view import hello
from .view import article
from .view import buscar
from .view import ola
from .view import name

from django.urls import include #Include é para importar urls de outros Apps(pode ser importado junto com path)
from clientes import urls as clients_urls #Referenciando o App Clientes e dando um nome a ele

#Proximos 2 importes para poder mostrar arquivos de mídia em tempo de desenvolvimento
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/',include(clients_urls)),#Referencia do App que estou chamando 
    path('ola/', ola),
    path('name/<str:name>',name),
    path('article/<int:year>', article),
    path('hello/', hello),
    path('buscar/<str:nome>', buscar)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Para poder mostrar arquivos de mídia em tempo de desenvolvimento
