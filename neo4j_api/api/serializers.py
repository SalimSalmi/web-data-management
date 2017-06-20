from api.models import Movie, Genre, Actor
from rest_framework import serializers



#         Scenario 1
# ---------------------------

class MovieActorSerializer(serializers.Serializer):
    fname = serializers.CharField()
    lname = serializers.CharField()
    mname = serializers.CharField()

class GenreSerializer(serializers.Serializer):
    genre = serializers.CharField()

class MovieSerializer(serializers.Serializer):
    idmovies = serializers.IntegerField()
    title = serializers.CharField()
    year = serializers.IntegerField()
    language = serializers.CharField()
    location = serializers.CharField()

    genres = GenreSerializer(many=True)
    actors = MovieActorSerializer(many=True)


#         Scenario 2
# ---------------------------

class ActorMovieSerializer(serializers.Serializer):
    idmovies = serializers.IntegerField()
    title = serializers.CharField()
    year = serializers.IntegerField()

class ActorDetailsSerializer(serializers.Serializer):
    fname = serializers.CharField()
    lname = serializers.CharField()
    mname = serializers.CharField()
    movies = ActorMovieSerializer(many=True)


#         Scenario 3
# ---------------------------

class ActorStatsSerializer(serializers.Serializer):
    fname = serializers.CharField()
    lname = serializers.CharField()
    mname = serializers.CharField()
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj):
        return len(obj.movies)


#         Scenario 4
# ---------------------------

class MovieGenreSerializer(serializers.Serializer):
    idmovies = serializers.IntegerField()
    title = serializers.CharField()

class GenreExpSerializer(serializers.Serializer):
    year = serializers.SerializerMethodField()
    genre = serializers.CharField()
    movies = serializers.SerializerMethodField()

    def get_movies(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = obj.movies.filter(year=year)
        serializer = MovieGenreSerializer(instance=qs, many=True)
        return serializer.data

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)


#         Scenario 5
# ---------------------------

class GenreStatsSerializer(serializers.Serializer):
    year = serializers.SerializerMethodField()
    genre = serializers.CharField()
    movies_count = serializers.SerializerMethodField()


    def get_movies_count(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = obj.movies.filter(year=year)
        return len(qs)

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)
