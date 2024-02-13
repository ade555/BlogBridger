from rest_framework import serializers
from django.db import transaction
from rest_framework.authtoken.models import Token

from .models import User
from posts.serializers import PostSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'posts']

    @transaction.atomic
    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'posts' in representation:
            for post_data in representation['posts']:
                post_data.pop('author', None)
        
        return representation
