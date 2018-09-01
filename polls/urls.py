from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/proveedor', views.add_proveedores, name='add_proveedor'),
    path('agregar/', views.add_licitaciones, name='add_licitacion'),
    path('listado/proveedores', views.list_proveedores, name='list_proveedores'),
    path('listado/licitaciones', views.list_licitaciones, name='list_licitaciones'),

]