from api.models import Movies, Genres, Actors, ActedIn
from rest_framework import serializers



#         Scenario 1
# ---------------------------

class MovieActorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Actors
        fields = ('fname','lname','mname')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genres
        fields = ('idgenres', 'genre',)

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True)
    actors = MovieActorSerializer(many=True)

    class Meta:
        model = Movies
        fields = ('idmovies', 'title', 'year', 'language', 'genres', 'location', 'actors')
        depth = 1



#         Scenario 2
# ---------------------------

class ActorMovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movies
        fields = ('idmovies', 'title', 'year',)
        ordering = ('year',)

class ActorDetailsSerializer(serializers.HyperlinkedModelSerializer):
    movies = ActorMovieSerializer(many=True)

    class Meta:
        model = Actors
        fields = ('fname','lname', 'movies')
        depth = 1


#         Scenario 3
# ---------------------------

class ActorStatsSerializer(serializers.HyperlinkedModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Actors
        fields = ('fname','lname', 'movies_count')
        depth = 1

    def get_movies_count(self, obj):
        return obj.movies.count()


#         Scenario 4
# ---------------------------

class MovieGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ('idmovies', 'title',)
        depth = 1


class GenreExpSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genres
        fields = ('genre', 'movies', 'year')
        depth = 1

    def get_movies(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = obj.movies.filter(year=year)
        serializer = MovieGenreSerializer(instance=qs, many=True)
        return serializer.data

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)


#         Scenario 5
# ---------------------------

class GenreStatsSerializer(serializers.HyperlinkedModelSerializer):
    movies_count = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    class Meta:
        model = Genres
        fields = ('genre', 'movies_count', 'year')

    def get_movies_count(self, obj):
        year = self.context['request'].query_params.get('year', None)
        qs = obj.movies.filter(year=year)
        return qs.count()

    def get_year(self, obj):
        return self.context['request'].query_params.get('year', None)
