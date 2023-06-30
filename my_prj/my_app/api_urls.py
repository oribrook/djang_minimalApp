from django.urls import path
from . import api_views 

urlpatterns = [        
    path('drf', api_views.test_drf),
    path('article', api_views.serve_article),
    path('site', api_views.serve_site),
]
