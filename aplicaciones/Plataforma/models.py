from django.db import models
from django.shortcuts import render, redirect

# Create your models here.
class Auto(models.Model):
    patente=models.CharField(primary_key=True,max_length=8)
    precio=models.IntegerField()
    km=models.IntegerField()
    tipo=models.CharField(max_length=1)
    disponibilidad=models.CharField(max_length=1)
    
    def __str__(self) -> str:
        return f"{self.patente} {self.precio} {self.km} {self.tipo} {self.disponibilidad}"
