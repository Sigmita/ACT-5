# app_Netflix/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs de Inicio
    path('', views.inicio_netflix, name='inicio_netflix'),

    # URLs para Usuario (CRUD)
    path('usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/actualizar/<int:id_usuario>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/actualizar/realizar/<int:id_usuario>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:id_usuario>/', views.borrar_usuario, name='borrar_usuario'),

    # URLs para Película (CRUD)
    path('peliculas/', views.ver_peliculas, name='ver_peliculas'),
    path('peliculas/agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('peliculas/actualizar/<int:id_pelicula>/', views.actualizar_pelicula, name='actualizar_pelicula'),
    path('peliculas/actualizar/realizar/<int:id_pelicula>/', views.realizar_actualizacion_pelicula, name='realizar_actualizacion_pelicula'),
    path('peliculas/borrar/<int:id_pelicula>/', views.borrar_pelicula, name='borrar_pelicula'),

# URLs para Listas de Favoritos (NUEVAS)
    path('listas/', views.ver_listas_favoritos, name='ver_listas_favoritos'),
    path('listas/agregar/', views.agregar_lista_favoritos, name='agregar_lista_favoritos'),
    path('listas/actualizar/<int:id_lista>/', views.actualizar_lista_favoritos, name='actualizar_lista_favoritos'),
    path('listas/realizar_actualizacion/<int:id_lista>/', views.realizar_actualizacion_lista_favoritos, name='realizar_actualizacion_lista_favoritos'),
    path('listas/borrar/<int:id_lista>/', views.borrar_lista_favoritos, name='borrar_lista_favoritos'),
]