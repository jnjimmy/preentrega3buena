from django.urls import path
from .views import crea_curso, lista_cursos, profesores, cursos, estudiantes, entregables, inicio, curso_formulario, busqueda_camada, buscar_camada

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_cursos),
    path("", inicio, name="Inicio"),
    path('profesores/', profesores, name="Profesores"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('curso-formulario/', curso_formulario, name="CursoFormulario"),
    path('busqueda-camada/', busqueda_camada, name="BusquedaCamada"),
    path('buscar-camada/', buscar_camada, name="BuscarCamada"),

]
