from rest_framework import serializers

from .models import Note

from .models import Body

from .models import Chisme



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'text', )
        
class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'text', )
class ChismeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'titulo', 'chisme' , )

