from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="home"),
     path('experiencias/', views.experiencias, name="experiencias"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('talleres/', views.talleres, name="talleres"),

    path('eventos/', views.eventos, name="eventos"),

    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<slug:slug_text>', views.post),
    path('eventos/<slug:slug_text>', views.evento_post),
  
    path('galerias/', views.galerias, name="galerias"),
    path('galerias/<int:id>', views.catalogogalerias),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)