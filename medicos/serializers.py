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

