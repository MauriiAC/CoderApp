from django.urls import path

from AppCoder.views import (
    cursos_view,
    cursos_buscar_view,
    cursos_todos_view,
    inicio_view,
    profesores_view,
    lista_profesores,
    crea_profesor,
    eliminar_profesor,
    editar_profesor,
    CursoList,
    CursoDetail,
    CursoCreate,
    CursoUpdate,
    CursoDelete
    )


app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("comisiones/", profesores_view),
    path("inicio/", inicio_view, name="inicio"),
    path("lista-profesores/", lista_profesores, name="lista-profesores"),
    path("crea-profesor/", crea_profesor, name="crea-profesor"),
    path("elimina-profesor/<int:id>", eliminar_profesor, name="elimina-profesor"),
    path("editar-profesor/<int:id>", editar_profesor, name="editar-profesor"),
    path("lista-cursos", CursoList.as_view(), name="lista-cursos"),
    path("detalle-cursos/<pk>", CursoDetail.as_view(), name="detalle-cursos"),
    path("crea-curso", CursoCreate.as_view(), name="crea-curso"),
    path("editar-curso/<pk>", CursoUpdate.as_view(), name="editar-curso"),
    path("eliminar-curso/<pk>", CursoDelete.as_view(), name="eliminar-curso"),
]
