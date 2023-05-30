from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class', views.MyClassView.as_view()),
]
