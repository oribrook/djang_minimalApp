from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notes', views.serve_notes),
    path('notes/cache', views.serve_notes_cached_manually),
    path('notes/cache_view', views.serve_notes_view_cache),
    path('notes/create', views.create_note),

]
