from api.models import Movie, Genre, Actor
from rest_framework import viewsets
from api.serializers import MovieSerializer, GenreSerializer, ActorDetailsSerializer, ActorStatsSerializer, GenreExpSerializer, GenreStatsSerializer
from rest_framework import generics


class MovieViewSet(viewsets.ModelViewSet):
    # queryset = Movie.objects.filter(title__contains="Star Wars",type=3)
    serializer_class = MovieSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        idmovies = self.request.query_params.get('id', None)
        if(idmovies):
            return Movie.nodes.filter(idmovies=idmovies,type="3")
        else:
            return Movie.nodes.filter(title__icontains=name,type="3")


class ActorDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorDetailsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', None)
        lname = self.request.query_params.get('lname', None)
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actor.nodes.filter(idactors=idactors)
        else:
            return Actor.nodes.filter(fname=fname,lname=lname)


class ActorStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorStatsSerializer

    def get_queryset(self):
        fname = self.request.query_params.get('fname', None)
        lname = self.request.query_params.get('lname', None)
        idactors = self.request.query_params.get('id', None)

        if(idactors):
            return Actor.nodes.filter(idactors=idactors)
        else:
            return Actor.nodes.filter(fname=fname,lname=lname)

class GenreExpViewSet(viewsets.ModelViewSet):
    serializer_class = GenreExpSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genre.nodes.filter(genre=genre)

class GenreStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GenreStatsSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre', None)

        return Genre.nodes.filter(genre=genre)
