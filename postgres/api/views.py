from api.models import Movies, Genres
from rest_framework import viewsets
from api.serializers import MovieSerializer, GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
