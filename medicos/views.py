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