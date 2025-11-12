# app_Netflix/admin.py
from django.contrib import admin
from .models import Usuario, Pelicula,ListaFavoritos# Importa también Pelicula

admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(ListaFavoritos)  # Registra el modelo Pelicula