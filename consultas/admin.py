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