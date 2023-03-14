from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import (api_view,
                             authentication_classes,
                             permission_classes)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", None)

    user = User.objects.create_user(username=username, password=password, email=email)

    return Response(f"new user created. id: {user.id}")


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def private(request):
    return Response(f"This is a private response. user is: {request.user.username}")


"""
    * in order to achieve separated permission per function under class view
      you will need to check manually if user is authenticated.
      The authenticated method should be defined in settings.py as:
      REST_FRAMEWORK = {
          'DEFAULT_AUTHENTICATION_CLASSES': [
              'rest_framework.authentication.BasicAuthentication',        
          ]
      }

    * in the following code, I also added check that right method was called
      into the right url. so, if user will call private-class-get with post, he will 
      get response of "Not allowed method!".

"""
class MyView(APIView):

    method_required = None
    
    ## uncomment the following will apply auth policy to all functions.
    # authentication_classes = [BasicAuthentication]    
    # permission_classes = [IsAuthenticated]

    def get(self, req):        
        return Response("returned from MyView-get")
    
    def post(self, req):        
        if not req.user.is_authenticated:
            return Response("Credential missing. No access!")    
        
        return Response("returned from MyView-post")

    def dispatch(self, request, *args, **kwargs):

        if self.method_required == "get" and request.method != 'GET':
            return HttpResponse("Not allowed method!")
        
        if self.method_required == "post" and request.method != 'POST':
            return HttpResponse("Not allowed method!")
        
        return super().dispatch(request, *args, **kwargs)
