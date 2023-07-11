from django.urls import path, include
from . import api_views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("articles", api_views.ArticleViewSet)

urlpatterns = [        
    path('drf', api_views.test_drf),
    path('article', api_views.serve_article),
    path('site', api_views.serve_site),
    path('', include(router.urls))
]
