from rest_framework import serializers
from .models import Todo, TodoShare, TodoAccessLog, UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'password']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'owner', 'title', 'description', 'category', 'due_date', 'status']


class TodoShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoShare
        fields = ['id', 'todo', 'shared_with', 'access_level']


class TodoAccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoAccessLog
        fields = ['id', 'todo', 'user', 'action', 'timestamp']
