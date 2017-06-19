from api.models import Movies, Genres, Actors
from rest_framework import viewsets
from api.serializers import MovieSerializer, GenreSerializer, ActorDetailsSerializer, ActorStatsSerializer, GenreExpSerializer, GenreStatsSerializer
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


class ActorDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorDetailsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', None)
        lname = self.request.query_params.get('lname', None)
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actors.objects.filter(idactors=idactors,type=3)
        else:
            return Actors.objects.filter(fname=fname,lname=lname)


class ActorStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorStatsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', None)
        lname = self.request.query_params.get('lname', None)
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actors.objects.filter(idactors=idactors,type=3)
        else:
            return Actors.objects.filter(fname=fname,lname=lname)

class GenreExpViewSet(viewsets.ModelViewSet):
    serializer_class = GenreExpSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genres.objects.filter(genre=genre)

class GenreStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GenreStatsSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genres.objects.filter(genre=genre)
