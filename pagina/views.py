from django.shortcuts import render, HttpResponse, redirect
from.models import Noticias, Galerias, Videos, Talleres, Eventos, CatalogoGalerias
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages



# Create your views here.


def inicio(request):
    return render(request, "inicio.html")

def experiencias(request):
    return render(request, "experiencias.html")


def nosotros(request):
    return render(request, "nosotros.html")


def talleres(request):
    queryset = request.GET.get("buscar")
    talleres = Talleres.objects.filter(status= True).order_by('-id')
   
    if queryset:
        talleres = Talleres.objects.filter(
           Q(titulo__icontains = queryset ) 
        ).distinct()
       
    paginator = Paginator(talleres, 8)
    page = request.GET.get('page')
    talleres = paginator.get_page(page)
    context = {"talleres": talleres}
    return render(request, "talleres.html", context)    








def noticias(request):
    queryset = request.GET.get("buscar")
    noticias = Noticias.objects.filter(status= True).order_by('-id')
    #noticias = Noticias.objects.filter(~Q(id__lt=6)).order_by('-id')   
    if queryset:
        noticias = Noticias.objects.filter(
           Q(titulo__icontains = queryset ) |
           Q(contenido__icontains = queryset )
        ).distinct()
       
    paginator = Paginator(noticias, 9)
    page = request.GET.get('page')
    noticias = paginator.get_page(page)
    context = {"noticias": noticias}
    return render(request, "noticias.html", context) 





def eventos(request):
    queryset = request.GET.get("buscar")
    eventos = Eventos.objects.filter(status= True).order_by('-id')
    
    if queryset:
        eventos = Eventos.objects.filter(
           Q(titulo__icontains = queryset )
        ).distinct()
       
    paginator = Paginator(eventos, 9)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    context = {"eventos": eventos}
    return render(request, "eventos.html", context) 






def post(request, slug_text):
    noticia = Noticias.objects.filter(slug=slug_text)
    if noticia.exists():
        noticia = noticia.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")

    context = {'noticia': noticia}

    return render(request, "post.html", context)  


def evento_post(request, slug_text):
    noticia = Eventos.objects.filter(slug=slug_text)
    if noticia.exists():
        noticia = noticia.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")

    context = {'noticia': noticia}

    return render(request, "evento_post.html", context) 









def galerias(request):


    galerias = Galerias.objects.filter()
    paginator = Paginator(galerias, 2)
    page = request.GET.get('page')
    galerias = paginator.get_page(page)
    context = {"galerias": galerias}
    return render(request, "galerias.html", context)



def catalogogalerias(request, id):


    catalogos = CatalogoGalerias.objects.filter(galeria_id=id)
    context = {"catalogos": catalogos}
    return render(request, "catalogo_galeria.html", context) 