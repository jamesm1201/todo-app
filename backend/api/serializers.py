from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
#This takes in JSON data and converts to Python equivalent and vice versa

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        #** splits arguments and passes from a dictionary
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notefields = ["id", "title", "content", "created_at", "author"]
        #Ensures authenticated user is the only author and cannot change
        extra_kwargs = {"author": {"read-only": True}}