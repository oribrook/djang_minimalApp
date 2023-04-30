from rest_framework.serializers import ModelSerializer

from my_app.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        exclude = ['user']
