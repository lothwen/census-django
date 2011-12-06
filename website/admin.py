from django.contrib import admin
from models import Chavales, Ramas

class ChavalesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'rama')
    search_fields = ('nombre', 'apellidos', 'rama', 'municipio')
    ordering = ('nombre','rama',)

admin.site.register(Chavales, ChavalesAdmin)
admin.site.register(Ramas)

