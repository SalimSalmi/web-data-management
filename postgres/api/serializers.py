from api.models import Movies, Genres, Actors
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movies
        fields = ('title', 'year', 'type')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genres
        fields = ('genre',)

class ActorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Actors
        fields = '__all__'
