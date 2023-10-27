from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GeneralFile
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("<h1> Welcome to Django minimal APP </h1>")


@api_view(['POST'])
def upload_file(request):
    
    # Get the uploaded file from the request
    uploaded_file = request.FILES.get('file')

    if uploaded_file:
        try:

            # Create a new instance of your model and assign the file
            gf = GeneralFile(file=uploaded_file)
            gf.save()

            # You can also do additional processing here if needed

            return JsonResponse({'message': 'File uploaded successfully.'}, 200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
