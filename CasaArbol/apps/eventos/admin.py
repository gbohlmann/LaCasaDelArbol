from django.contrib import admin
from .models import Categoria,Eventos

# Register your models here.
class categoria_admin(admin.ModelAdmin):
    list_display=("nombre",)
    list_filter=("nombre",)
    
class eventos_admin(admin.ModelAdmin):
    list_display=("titulo",)
    list_filter=("categoria","fecha_creacion",)    
admin.site.register(Categoria,categoria_admin)
admin.site.register(Eventos,eventos_admin)