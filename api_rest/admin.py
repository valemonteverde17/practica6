from django.contrib import admin
from .models import Comida, Bebida, Snack

# Register your models here.
class ComidaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creado',)
    
admin.site.register(Comida,ComidaAdmin)


class BebidaAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creado',)
    
admin.site.register(Bebida,BebidaAdmin)


class SnackAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creado',)
    
admin.site.register(Snack,SnackAdmin)

