from django.contrib import admin

from .models import Categoria, Noticia,Comentarios

# Register your models here.
class categoria_admin(admin.ModelAdmin):
    list_display=("nombre",)
    list_filter=("nombre",)
class noticia_admin(admin.ModelAdmin):
    list_display=("titulo",)
    list_filter=("categorias","publicado",)
class comentarios_admin(admin.ModelAdmin):
    list_display=("autor","creado",)
    list_filter=("creado","autor",)    


admin.site.register(Categoria,categoria_admin)
admin.site.register(Noticia,noticia_admin)
admin.site.register(Comentarios,comentarios_admin)