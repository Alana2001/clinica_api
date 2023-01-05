from django.db import models
from clientes.models import Cliente
from medicos.models import Agenda

class Consulta(models.Model):
    
    CHOICES = (
		('Agendada', 'Agendada'),
		('Cancelada', 'Cancelada'),
	)
	
    agendamentos = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='Consulta')
    consulta_dos_clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", blank=False)

    def __str__(self):
        return f'{self.agendamentos} - {self.consulta_dos_clientes}'
