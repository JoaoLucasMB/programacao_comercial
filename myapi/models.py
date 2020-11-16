from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=60)
    idade = models.CharField(max_length=3)
    
    def __str__(self):
        return self.nome
     