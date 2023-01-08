# DESAFIO CLINICA_API

## Desenvolvedora:
+ Discente: Alana Letícia Lustosa de Castro
+ IFPI - Instituto Federal do Piauí - Campus Corrente
+ Docente: @fgsantosti

## Informações do Projeto:
+ Você deverá implementar uma API (Interface de Programação de Aplicação) na qual
gestor da clínica (superusuário) poderá cadastrar especialidades, médicos e
disponibilizar horários nos quais os clientes poderão marcar as consultas.

## Faça as seguintes etapas:
 Criando pasta:
 ```python
 mkdir clinica_api
```

Entrar na pasta:
```python
 cd clinica_api
```

## Criando o ambiente virtual:
Faça o seguinte comando:
```python
 virtualenv minhaenv
```

Ative o seu Ambiente Virtual:
```python
 . minhaenv/bin/activate
```

## Instale o framework Django::
Faça o comando:
```python
 pip install django
```

## Criando o projeto Django Clinica Api:
Use o seguinte comando para criar a config:
```python
 django-admin startproject core .
```

## Mudando as configurações dentro do core:
```python
 LANGUAGE_CODE = 'en-us'
 TIME_ZONE = 'UTC'
```

## Instalando o Django Rest Framework:
```python
 pip install djangorestframework
 ```

## Instalando o Markdown:
```python
 pip install markdown
 ```

## Instalando o django-filter:
```python
 pip install django-filter
```

## Criando a primeira aplicação:
```python
python manage.py startapp medicos
```

## Realizando a instalação das app's criadas:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'medicos', 
]
```
## Criando os modelos para nossa clinica
+ Primeira etapa do nosso modelo de medicos:
```python
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
```
## Criando a segunda aplicação:
```python
python manage.py startapp clientes
```

## Realizando a instalação das app's criadas:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'medicos',
    'clientes',
]
```
## Criando os modelos para nossa clinica
+ Segunda etapa do nosso modelo de clientes:
```python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    sexo = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome 
```

## Criando a segunda aplicação:
```python
python manage.py startapp consultas
```

## Realizando a instalação das app's criadas:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'medicos',
    'clientes',
    'consultas',
]
```
## Criando os modelos para nossa clinica
+ Terceira etapa do nosso modelo de consultas:
```python
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
```

## Criando tabelas para nossos modelos no banco de dados:
+ O último passo é adicionar nosso novo modelo ao banco de dados. 

```python
python manage.py makemigrations medicos
```

+ Faça o mesmo com clientes:

```python
python manage.py makemigrations clientes
```
+ E por último consultas:
```python
python manage.py makemigrations consultas
```

## Django Admin:
+ Vamos criar um administrador:
```python
python manage.py createsuperuser
```

## Configure o seu arquivo medicos/admin.py
```python
from django.contrib import admin
from medicos.models import Especialidades, Cadastrar_Medicos, Agenda

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome')
    search_fields =['nome']
    list_per_page = 20
    ordering = ('nome',)

class Cadastrar_MedicosAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome', 'CRM', 'email', 'telefone', 'especialidade'
    ]
    list_display_links = ('id', 'CRM')
    search_fields =['CRM']
    list_per_page = 20

class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'medico', 'data', 'horario'
    ]
    list_display_links = ('id', 'data')
    search_fields =['medico']
    list_per_page = 20
    
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(Cadastrar_Medicos, Cadastrar_MedicosAdmin)
admin.site.register(Agenda, AgendaAdmin)
```

## Configure o seu arquivo clientes/admin.py
```python
from django.contrib import admin
from .models import Cliente
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome', 'cpf', 'email', 'sexo', 'telefone'
    ]
    list_display_links = ('id', 'nome', 'cpf')
    search_fields =['nome']
    list_per_page = 25
    ordering = ('nome',)

admin.site.register(Cliente, ClienteAdmin)
```

## Configure o seu arquivo consultas/admin.py
```python
from django.contrib import admin
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'agendamentos', 'consulta_dos_clientes',
    ]
    list_display_links = ('id', 'agendamentos')
    search_fields =['agendamentos']
    list_per_page = 25
    
admin.site.register(Consulta, ConsultaAdmin)
```

## Vamos startar o servidor web:
```python
python manage.py runserver #startando o servidor
```
