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