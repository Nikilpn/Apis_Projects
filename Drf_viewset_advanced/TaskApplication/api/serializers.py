from api.models import Task
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    user_object=serializers.StringRelatedField()
    class Meta:
        model=Task

        fields="__all__"

        read_only_fields=["id","assigned_date","user_object"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=["id","username","password"]
        read_only_fields=["id"]


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user