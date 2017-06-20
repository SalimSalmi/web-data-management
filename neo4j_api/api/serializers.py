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

    class Meta:
        model = Movie
        fields = ('idmovies', 'title', 'year',)
        ordering = ('year',)

class ActorDetailsSerializer(serializers.Serializer):
    movies = ActorMovieSerializer(many=True)

    class Meta:
        model = Actor
        fields = ('fname','lname', 'movies')
        depth = 1


#         Scenario 3
# ---------------------------

class ActorStatsSerializer(serializers.Serializer):
    movies_count = serializers.SerializerMethodField()
    

    class Meta:
        model = Actor
        fields = ('fname','lname', 'movies_count')
        depth = 1

    def get_movies_count(self, obj):
        return obj.movies.count()


#         Scenario 4
# ---------------------------

class MovieGenreSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ('idmovies', 'title',)
        depth = 1


class GenreExpSerializer(serializers.Serializer):
    movies = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('genre', 'movies', 'year')
        depth = 1

    def get_movies(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = Movie.nodes.filter(year=year)
        serializer = MovieGenreSerializer(instance=qs, many=True)
        return serializer.data

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)


#         Scenario 5
# ---------------------------

class GenreStatsSerializer(serializers.Serializer):
    movies_count = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('genre', 'movies_count', 'year')
        depth = 1

    def get_movies_count(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = Movie.nodes.filter(year=year)
        return qs.count()

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)
