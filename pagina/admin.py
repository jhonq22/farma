from django.contrib import admin
from django.db import models
from .models import Categoria, Noticias,Galerias, Videos, CatalogoGalerias, Talleres, Eventos

# Register your models here.
class NoticiasAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','fecha_publicacion','categoria','status',)
    date_hierarchy="fecha_publicacion"



class TalleresAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','fecha_publicacion','status',)
    date_hierarchy="fecha_publicacion"


class EventosAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','fecha_publicacion','status',)
    date_hierarchy="fecha_publicacion"    


class GaleriasAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','imagen_principal','status')  



class CatalogosAdmin(admin.ModelAdmin):
    search_fields = ['galeria']
    list_display = ('galeria','imagen_principal')



admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Categoria)
admin.site.register(Galerias, GaleriasAdmin)
admin.site.register(Videos)
admin.site.register(CatalogoGalerias, CatalogosAdmin)
admin.site.register(Talleres)
admin.site.register(Eventos)