from django.db import models
# Create your models here.

class Catedratico(models.Model):
    cedula_identidad = models.CharField(max_length=50, unique=True)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    activo = models.BooleanField(blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombres
#DateField
class Reporte_semanal(models.Model):
     catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
     fecha_entrega = models.DateTimeField(auto_now_add=True)
     nro_semana = models.IntegerField()
#     def __str__(self):
#        return self.fecha_entrega
    
class Materia(models.Model):
    materia = models.CharField(max_length=200)
    codigo_materia = models.CharField(max_length=10)
    def __str__(self):
        return self.materia
    
class Paralelo(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    paralelo = models.CharField(max_length=10)
    def __str__(self):
        return self.paralelo

class Catedratico_materia_paralelo(models.Model):
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    def __str__(self):
        return self.catedratico
    
class Tema(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    indice =models.CharField(max_length=10)
    tema = models.CharField(max_length=500)
    def __str__(self):
        return self.tema
    
class Contenido(models.Model):
    tema= models.ForeignKey(Tema, on_delete=models.CASCADE)
    indice =models.CharField(max_length=10)
    contenido=models.CharField(max_length=500)
    def __str__(self):
        return self.contenido
    
class Avance_materia(models.Model):
    reporte_semanal = models.ForeignKey(Reporte_semanal, on_delete=models.CASCADE)
    paralelo = models.ForeignKey(Paralelo,on_delete=models.CASCADE)
    
class Avance_tema(models.Model):
    avance_materia = models.ForeignKey(Avance_materia, on_delete=models.CASCADE)
    tema=models.ForeignKey(Tema,on_delete=models.CASCADE)
    dificultades = models.CharField(max_length=500)
    sugerencias = models.CharField(max_length=500) 
    
class Avance_contenido(models.Model):
    avance_tema = models.ForeignKey(Avance_tema, on_delete=models.CASCADE)
    contenido=models.ForeignKey(Contenido,on_delete=models.CASCADE)


