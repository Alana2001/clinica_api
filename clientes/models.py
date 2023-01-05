from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    sexo = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome 
