from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from consultas.serializers import ConsultasSerializer
from consultas.models import Consulta

class ConsultasViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Consulta.objects.all()
    serializer_class = ConsultasSerializer