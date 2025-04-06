from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from django.db.models import Avg
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.review_movie.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        return None

    def validate_release_year(self, value):
        if value.year < 1920:
            raise serializers.ValidationError("Não é possível cadastrar filmes anteriores a 1920.")
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("A quantidade de caracteres excedeu 200.")
        return value
    
    
class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_year', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.review_movie.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        return None
