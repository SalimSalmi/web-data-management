from api.models import Movies, Actors,Genres
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
        name = self.request.query_params.get('name', '')
        idmovies = self.request.query_params.get('id', None)

        if(idmovies):
            return Movies.objects(idmovies=idmovies,type=3)
        else:
            return Movies.objects(title__icontains=name,type=3)



class ActorDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorDetailsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', '')
        lname = self.request.query_params.get('lname', '')
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actors.objects.filter(idactors=idactors)
        else:
            return Actors.objects.filter(fname=fname,lname=lname)


class ActorStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorStatsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', '')
        lname = self.request.query_params.get('lname', '')
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actors.objects.filter(idactors=idactors)
        else:
            return Actors.objects.filter(fname=fname,lname=lname)

class GenreExpViewSet(viewsets.ModelViewSet):
    serializer_class = GenreExpSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genres.objects.filter(genre__icontains=genre)

class GenreStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GenreStatsSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genres.objects(genre__icontains=genre)
