from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup),
    path('private', views.private),

    # class-view example
    path('class-get', views.MyView.as_view(method_required='get')),
    path('private-class-post', views.MyView.as_view(method_required='post')),
]
