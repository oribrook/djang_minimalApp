from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notes-auth', views.NotesViewSet)


urlpatterns = [
    path('', views.home),    
    path('signup', views.signup),
    path('public-notes', views.serve_notes_pagination),    
    path('obtain-token', obtain_auth_token),
    path('', include(router.urls)),
    path('check-token', views.check_token),

]
