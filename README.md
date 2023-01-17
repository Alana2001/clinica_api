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
 . minhaenv/Scripts/activate
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

O Django preparou um arquivo de migração que precisamos aplicar ao nosso banco de dados:

+ Faça o seguinte comando com os 3 apps:

```python
python manage.py migrate medicos
```
+ O próximo:

```python
python manage.py migrate clientes
```

+ E por último:
```python
python manage.py migrate consultas
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

+ Vamos acessar a área do administrador do sistema que já vem prontinho para gente graças ao framework Django, para isso iremos usamos o segunte endereço no navegador de sua preferência:
```python
http://127.0.0.1:8000/admin/
```

## Serialização:
Crie um arquivo no diretório de medicos denominado serializers.py (medicos/serializer.py) e adicione o seguinte código.

```python
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from medicos.models import Especialidades, Cadastrar_Medicos, Agenda

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = ['nome']
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

class Cadastrar_MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastrar_Medicos
        fields = ['nome', 'CRM', 'email', 'telefone', 'especialidade']
        verbose_name = 'Cadastar_Medico'
        verbose_name_plural = 'Cadastrar_Medicos'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['medico', 'data', 'horario']
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

class ListaEspecialidadesSerializer(serializers.ModelSerializer):
    especialidades_nome = serializers.ReadOnlyField(source='especialidades.nome')
    class Meta:
        model = Especialidades
        fields = ['especialidades_nome',]

class ListaMedicosCadastradosSerializer(serializers.ModelSerializer):
    medicoscadastrados_nome = serializers.ReadOnlyField(source='medicoscadastrados.nome')
    class Meta:
        model = Cadastrar_Medicos
        fields = ['medicoscadastrados_nome',]

class ListaAgendamentosSerializer(serializers.ModelSerializer):
    agendamentos_nome = serializers.ReadOnlyField(source='agendamentos.nome')
    class Meta:
        model = Agenda
        fields = ['agendamentos_nome',]
```

+ Faça o mesmo para clientes:

Crie um arquivo no diretório de clientes denominado serializers.py (clientes/serializer.py) e adicione o seguinte código.

```python
from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
```

+ Faça o mesmo para consultas:

Crie um arquivo no diretório de consultas denominado serializers.py (consultas/serializer.py) e adicione o seguinte código.

```python
from rest_framework import serializers
from consultas.models import Consulta

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
```

## Views - Escrevendo visualizações regulares do Django usando nosso Serializer:

Vamos ver como podemos escrever algumas visualizações de API usando nossa nova classe Serializer. 

+ Edite o arquivo medicos/views.py e adicione o seguinte:

```python
from django.db.models.query import QuerySet
from rest_framework import permissions
from medicos.models import Especialidades, Cadastrar_Medicos, Agenda
from django.shortcuts import render

from rest_framework import serializers, viewsets, generics
from medicos.serializers import EspecialidadesSerializer, Cadastrar_MedicosSerializer, AgendaSerializer, ListaEspecialidadesSerializer, ListaMedicosCadastradosSerializer, ListaAgendamentosSerializer
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EspecialidadesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as especialidades"""
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    #authentication_classes = [BaseAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class Cadastrar_MedicosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os medicos cadastrados"""
    queryset = Cadastrar_Medicos.objects.all()
    serializer_class = Cadastrar_MedicosSerializer
    #authentication_classes = [BaseAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AgendaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os agendamentos"""
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    #authentication_classes = [BaseAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ListaEspecialidadesSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        queryset = Especialidades.objects.filter(especialidade_id=self.kwargs['pk']) 
        return queryset
    
    serializer_class = ListaEspecialidadesSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMedicosCadastradosSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        queryset = Cadastrar_Medicos.objects.filter(medicoscadastrados_id=self.kwargs['pk']) 
        return queryset
    
    serializer_class = ListaMedicosCadastradosSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAgendamentosSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        queryset = Agenda.objects.filter(agendaementos_id=self.kwargs['pk']) 
        return queryset
    
    serializer_class = ListaAgendamentosSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]
```

+ Edite o arquivo clientes/views.py e adicione o seguinte:

```python
from django.shortcuts import render
from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
```

+ Edite o arquivo consultas/views.py e adicione o seguinte:

```python
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from consultas.serializers import ConsultasSerializer
from consultas.models import Consulta

class ConsultasViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultasSerializer
```

## Urls - Precisamos conectar essas visualizações:

### Suas URLs no Django REST!

Queremos que http://127.0.0.1:8000/ seja a página inicial da nossa clinica API e exiba uma as urls que configuramos anteriormente.

Abra o arquivo clinica_api/core/urls.py no seu editor e veja o que aparece:


```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from medicos.views import EspecialidadesViewSet, Cadastrar_MedicosViewSet, AgendaViewSet, ListaEspecialidadesSerializer, ListaMedicosCadastradosSerializer, ListaAgendamentosSerializer
from clientes.views import ClientesViewSet
from consultas.views import ConsultasViewSet

router = routers.DefaultRouter()
router.register('Especialidades', EspecialidadesViewSet, basename='Especialidades')
router.register('Cadastrar_Medicos', Cadastrar_MedicosViewSet, basename='Cadastrar_Medicos')
router.register('Agenda', AgendaViewSet, basename='Agenda')
router.register('Clientes', ClientesViewSet, basename='Clientes')
router.register('Consultas', ConsultasViewSet, basename='Consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('clientes/', include('clientes.urls', namespace="clientes")),
    path('consultas/', include('consultas.urls', namespace="consultas")),
]
```

+ Vamos startar o servidor web

```python
python manage.py runserver #startando o servidor
```


```python
http://127.0.0.1:8000/
```

Agora podemos vizualizar a página de API Root da nossa clinica API.
