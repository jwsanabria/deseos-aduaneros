from django.contrib import admin
from .models import *

# Register your models here.
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class DeseoAdmin(admin.ModelAdmin):
    list_display = ('deseo', 'personaje')
    search_fields = ('deseo',)


admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Deseo, DeseoAdmin)

