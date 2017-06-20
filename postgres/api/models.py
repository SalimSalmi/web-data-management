# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Actors(models.Model):
    idactors = models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=1023, blank=True, null=True)
    fname = models.CharField(max_length=1023, blank=True, null=True)
    mname = models.CharField(max_length=1023, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    movies = models.ManyToManyField(
        'Movies',
        through = 'ActedIn',
        related_name = 'movies_of_actors'
        )

    class Meta:
        managed = False
        db_table = 'actors'

class Genres(models.Model):
    idgenres = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=511, blank=True, null=True)

    movies = models.ManyToManyField(
        'Movies',
        through = 'MoviesGenres',
        related_name = 'movies_of_genre'
        )

    class Meta:
        managed = False
        db_table = 'genres'

class Movies(models.Model):
    idmovies = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1023, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=63, blank=True, null=True)
    language = models.CharField(max_length=63, blank=True, null=True)

    actors = models.ManyToManyField(
        'Actors',
        through = 'ActedIn',
        related_name = 'actors_of_movie'
    )

    genres = models.ManyToManyField(
        'Genres',
        through = 'MoviesGenres',
        related_name = 'genres_of_movie'
    )

    class Meta:
        managed = False
        db_table = 'movies'
        ordering = ('-year','title')


class ActedIn(models.Model):
    idacted_in = models.AutoField(primary_key=True)
    idseries = models.IntegerField(blank=True, null=True)
    character = models.CharField(max_length=2047, blank=True, null=True)
    billing_position = models.IntegerField(blank=True, null=True)

    idmovies = models.ForeignKey('Movies', db_column="idmovies", on_delete=models.CASCADE)
    idactors = models.ForeignKey('Actors', db_column="idactors", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'acted_in'

class MoviesGenres(models.Model):
    idmovies_genres = models.AutoField(primary_key=True)
    idmovies = models.ForeignKey('Movies', db_column="idmovies", on_delete=models.CASCADE)
    idgenres = models.ForeignKey('Genres', db_column="idgenres", on_delete=models.CASCADE)
    idseries = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_genres'
