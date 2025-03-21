

from rest_framework import serializers
from api.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model =Movie
        fields = '__all__'
        read_only_fields = ['id']
