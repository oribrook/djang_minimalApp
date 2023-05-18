from django.urls import path
from . import views, paginators

urlpatterns = [
    path('', views.home),
    path('notes', views.serve_notes),
    path('notes_pagination', views.serve_notes_pagination),
    path('notes_pagination2', paginators.NotePagination.as_view()),
]
