from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notes', views.serve_notes),
    path('notes/cache', views.serve_notes_cached),
    path('notes/create', views.create_note),

]
