from django.db import models
from datetime  import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    igredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=200)
    date_receita= models.DateTimeField(default=datetime.now, blank=True)