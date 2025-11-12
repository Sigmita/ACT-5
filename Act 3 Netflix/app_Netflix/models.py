# app_Netflix/models.py
from django.db import models

# ==========================================
# MODELO: USUARIO
# ==========================================
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    tipo_membresia = models.CharField(max_length=100)
    ultimo_acceso = models.DateTimeField(auto_now=True)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

# ==========================================
# MODELO: PELICULA
# ==========================================
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    ano_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=100)
    clasificacion_edad = models.CharField(max_length=50)
    duracion_minutos = models.IntegerField()
    director = models.CharField(max_length=255)
    idioma_original = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} ({self.ano_lanzamiento})"

# ==========================================
# MODELO: LISTA_FAVORITOS (Sigue comentado)
# ==========================================
# class ListaFavoritos(models.Model):
#     categoria_lista = models.IntegerField()
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='listas_favoritos')
#     pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='en_listas_favoritos')
#     fecha_adicion = models.DateField(auto_now_add=True)
#     orden_en_lista = models.IntegerField()
#     visto_en_lista = models.BooleanField(default=False)
#     notas_personales = models.TextField(blank=True, null=True)

#     class Meta:
#         unique_together = ('usuario', 'pelicula')

#     def __str__(self):
#         return f"Lista de {self.usuario.nombre} - {self.pelicula.titulo}"
class ListaFavoritos(models.Model):
    categoria_lista = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='listas_favoritos')
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='en_listas_favoritos')
    fecha_adicion = models.DateField(auto_now_add=True)
    orden_en_lista = models.IntegerField()
    visto_en_lista = models.BooleanField(default=False)
    notas_personales = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f"Lista de {self.usuario.nombre} - {self.pelicula.titulo}"