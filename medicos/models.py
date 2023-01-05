from django.db import models

class Especialidades(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome
    
class Cadastrar_Medicos(models.Model):
    nome = models.CharField(max_length=200)
    CRM = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.CASCADE, related_name="medicos")

    def __str__(self):
        return self.nome
    
class Agenda(models.Model):
    medico = models.ForeignKey(Cadastrar_Medicos, on_delete=models.CASCADE, verbose_name="Cadastrar_Medicos") 
    data = models.DateField()
    
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "14:00 ás 15:00"),
        ("5", "16:00 ás 17:00"),
    )
    horario = models.CharField(max_length=15, choices=Horarios)
        
    def __str__(self):
        return f'{self.medico} - {self.get_horario_display()}'
