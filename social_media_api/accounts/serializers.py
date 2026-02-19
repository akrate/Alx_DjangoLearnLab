from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Using serializers.CharField() for specific fields as requested
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Using get_user_model().objects.create_user as requested
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        # Automatically create a token for the new user
        Token.objects.create(user=user)
        return user