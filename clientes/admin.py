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
