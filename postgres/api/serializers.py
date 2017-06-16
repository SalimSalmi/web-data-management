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

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    movies_count = ActorMovieSerializer(many=True)

    class Meta:
        model = Actors
        fields = ('fname','lname', 'movies_count',)
        depth = 1

    def get_movies_count(self, obj):
        return obj.movies.count()
