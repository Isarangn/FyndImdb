from rest_framework import serializers
from .models import Movie, Genre
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'imdb_score', 'popularity', 'director', 'genre')

class UserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = ['id', 'username']