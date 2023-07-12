from django.db import models

# Create your models here.
"""
# One to Many
class Empresa(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Videojuego(models.Model):
    name = models.CharField(max_length = 150)
    empresa = models.Foreignkey(Empresa, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
"""

"""
Many to Many

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length = 50)
    movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return self.name
"""