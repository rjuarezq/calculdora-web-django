from django.urls import path
#from . import views
from operaciones.views import Home
from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),  
    path('resultado', views.calculation, name='resultado'),
    path('repositorio', views.red_github, name='repositorio')
]
