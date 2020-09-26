from django.contrib import admin
from imagens.models import Imagem

# Register your models here.

class ListandoImagens(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'foto', 'data')
    list_display_links = ('id', 'descricao') 

admin.site.register(Imagem, ListandoImagens)