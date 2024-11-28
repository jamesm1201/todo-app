from django.contrib.auth.models import User
from rest_framework import serializers

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