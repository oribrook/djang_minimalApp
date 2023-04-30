from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.serve_notes, name='notes'),
    path('notes_pagination', views.serve_notes_pagination, name='notes_pagination'),
]
