from django.db import models


class Contato(models.Model):
    email = models.EmailField("E-mail")
    telefone = models.CharField("Telefone", max_length=13)
    data_aniversario = models.DateTimeField("Data de Aniversário")
    peso = models.FloatField("Peso")
