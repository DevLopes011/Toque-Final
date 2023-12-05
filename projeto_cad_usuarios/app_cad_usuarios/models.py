from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)  
    email = models.EmailField(unique=True)  
    cpf = models.CharField(max_length=14)  
    endereco = models.TextField()  
    senha = models.CharField(max_length=255)  
