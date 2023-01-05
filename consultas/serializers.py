from rest_framework import serializers
from consultas.models import Consulta

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
    