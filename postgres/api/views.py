from api.models import Movies, Genres, Actors
from rest_framework import viewsets
from api.serializers import MovieSerializer, GenreSerializer, ActorSerializer
from rest_framework import generics


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Movies.objects.filter(title__contains="Star Wars",type=3)
    serializer_class = MovieSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        idmovies = self.request.query_params.get('id', None)

        if(idmovies):
            return Movies.objects.filter(idmovies=idmovies,type=3)
        else:
            return Movies.objects.filter(title__contains=name,type=3)


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', None)
        lname = self.request.query_params.get('lname', None)
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actors.objects.filter(idactors=idactors,type=3)
        else:
            return Actors.objects.filter(fname=fname,lname=lname)


# SELECT  m.year, m.language, a.fname, a.lname, ai.character
# FROM movies m JOIN acted_in ai ON (ai.idmovies=m.idmovies) JOIN actors a ON (a.idactors=ai.idactors)
# WHERE (m.idmovies = 396962 OR m.title LIKE '%Terminator%') AND TYPE=3 ORDER BY  ai.billing_position;
