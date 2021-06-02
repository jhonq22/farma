from django.db import models
from django.db.models.signals import pre_save
from web.utils import unique_slug_generator
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=80, verbose_name='Categoria')

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']
        db_table = 'categorias'


class Galerias(models.Model):
    titulo = models.CharField(max_length=80, verbose_name='Nombre Galería')
    slug = models.SlugField(max_length=200, null=True, blank=True)
    imagen_principal = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Galería')


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ['id']
        db_table = 'galerias'  



class CatalogoGalerias(models.Model):
    galeria = models.ForeignKey(Galerias, on_delete=models.CASCADE)
    imagen_principal = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.galeria.titulo
    

    class Meta:
        verbose_name = 'Catologo de Galeria'
        verbose_name_plural = 'Catalogo de Galerias'
        ordering = ['id']
        db_table = 'catalogo_galerias'






class Videos(models.Model):
    titulo = models.CharField(max_length=80, null=True, blank=True, verbose_name='Titulo Youtube')
    link = models.CharField(max_length=120, null=True, blank=True, verbose_name='Link Youtube')
    status = models.BooleanField(default= True, verbose_name='Estatus Link Youtube')
    


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['id']
        db_table = 'videos'



class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    fecha_publicacion = models.DateTimeField(auto_now_add= True, null=True)
    imagen_principal = models.ImageField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Publicación')


    def __str__(self):
        return self.titulo  


    class Meta:
       verbose_name = 'Noticia'
       verbose_name_plural = 'Noticias'
       ordering = ['id']
       db_table = 'noticias'





class Eventos(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Nombre Evento')
    contenido = RichTextField()
    fecha_publicacion = models.DateTimeField(auto_now_add= True, null=True)
    imagen_principal = models.ImageField(null=False, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default= True, verbose_name='Estatus Publicación')


    def __str__(self):
        return self.titulo  


    class Meta:
       verbose_name = 'Evento'
       verbose_name_plural = 'Eventos'
       ordering = ['id']
       db_table = 'eventos'




class Talleres(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Nombre Taller')
    fecha_publicacion = models.DateTimeField(auto_now_add= True, null=True)
    autor = models.CharField(max_length=200, verbose_name='Autor Taller')
    link = models.CharField(max_length=120, null=True, blank=True, verbose_name='Link del Taller')
    status = models.BooleanField(default= True, verbose_name='Estatus Publicación')


    def __str__(self):
        return self.titulo  


    class Meta:
       verbose_name = 'Taller'
       verbose_name_plural = 'Talleres'
       ordering = ['id']
       db_table = 'talleres'







def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Noticias)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Eventos)
     
