from api.models import Movies, Genres, Actors
from rest_framework import viewsets
from api.serializers import MovieSerializer, GenreSerializer, ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movies.objects.filter(title="Star Wars: The Last Jedi")
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class ActorFromMovieViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


# SELECT  m.year, m.language, a.fname, a.lname, ai.character
# FROM movies m JOIN acted_in ai ON (ai.idmovies=m.idmovies) JOIN actors a ON (a.idactors=ai.idactors)
# WHERE (m.idmovies = 396962 OR m.title LIKE '%Terminator%') AND TYPE=3 ORDER BY  ai.billing_position;
