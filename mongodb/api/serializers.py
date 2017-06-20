from api.models import Movies, Actors, Genres
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers



#         Scenario 1
# ---------------------------

class MovieActorSerializer(mongoserializers.DocumentSerializer):

    class Meta:
        model = Actors
        fields = ('fname','lname','mname')

class GenreSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Genres
        fields = ('genre',)

class MovieSerializer(mongoserializers.DocumentSerializer):
    genres = GenreSerializer(many=True)
    actors = MovieActorSerializer(many=True)

    class Meta:
        model = Movies
        fields = ('idmovies', 'title', 'year', 'language', 'genres', 'location', 'actors')

#         Scenario 2
# ---------------------------

class ActorMovieSerializer(mongoserializers.DocumentSerializer):

    class Meta:
        model = Movies
        fields = ('idmovies', 'title', 'year',)
        ordering = ('year',)

class ActorDetailsSerializer(mongoserializers.DocumentSerializer):
    movies = ActorMovieSerializer(many=True)

    class Meta:
        model = Actors
        fields = ('fname','lname', 'movies')
        depth = 1


#         Scenario 3
# ---------------------------

class ActorStatsSerializer(mongoserializers.DocumentSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Actors
        fields = ('fname','lname', 'movies_count')
        depth = 1

    def get_movies_count(self, obj):
        return len(obj.movies)


#         Scenario 4
# ---------------------------

class MovieGenreSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Movies
        fields = ('idmovies', 'title',)


class GenreExpSerializer(mongoserializers.DocumentSerializer):
    movies = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genres
        fields = ('genre', 'movies', 'year')

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)

    def get_movies(self, obj):
        year = self.context['request'].query_params.get('year', None)
        m = [movie for movie in obj.movies if movie.year == int(year)]
        serializer = MovieGenreSerializer(instance=m, many=True)
        return serializer.data



#         Scenario 5
# ---------------------------

class GenreStatsSerializer(mongoserializers.DocumentSerializer):
    movies_count = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genres
        fields = ('genre', 'movies_count', 'year')

    def get_movies_count(self, obj):
        year = self.context['request'].query_params.get('year', None)
        m = [movie for movie in obj.movies if movie.year == int(year)]
        return len(m)

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)
