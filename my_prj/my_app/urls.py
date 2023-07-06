from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SiteViewSet, home


router = DefaultRouter()
router.register('sites', SiteViewSet)


urlpatterns = [
    # ...    
    path('', home),
    path('', include(router.urls)),
]
