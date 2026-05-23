from django.urls import path
from . import views
urlpatterns = [
    path('calculadora/',views.calculadoraV,name="calculadoraU"),  
    path('suma/', views.sumaV, name='sumaU'),
    path('resta/', views.restaV, name='restaU'),
    path('multiplicacion/', views.multiplicacionV, name='multiplicacionU'),
    path('division/', views.divisionV, name='divisionU'),    
    path('', views.inicioV, name='inicioU'),  
]
