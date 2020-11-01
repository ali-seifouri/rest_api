from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """serializer for the user objects"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        return  get_user_model().objects.create_user(**validated_data)