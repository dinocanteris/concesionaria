
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarAuto/',views.registrarAuto),
    path('edicionAuto/<patente>',views.edicionAuto),
    path('borrarAuto/<patente>',views.borrarAuto),
    path('editarAuto/',views.editarAuto)
]
