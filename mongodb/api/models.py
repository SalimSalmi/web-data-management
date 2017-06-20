# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from mongoengine import Document, EmbeddedDocument, fields


class Actors(Document):
    idactors = fields.IntField()
    lname = fields.StringField()
    fname = fields.StringField()
    mname = fields.StringField()
    gender = fields.IntField()
    number = fields.IntField()

    movies = fields.ListField(fields.ReferenceField('Movies'))


class Genres(EmbeddedDocument):
    genre = fields.StringField()

class Movies(Document):
    idmovies = fields.IntField()
    title = fields.StringField()
    year = fields.IntField()
    number = fields.IntField()
    type = fields.IntField()
    location = fields.StringField()
    language = fields.StringField()

    actors = fields.ListField(fields.ReferenceField('Actors'))
    genres = fields.EmbeddedDocumentListField(Genres)


#
#
# class ActedIn(models.Model):
#     idacted_in = models.AutoField()
#     idseries = models.IntegerField()
#     character = models.StringField(max_length=2047, blank=True, null=True)
#     billing_position = models.IntegerField(blank=True, null=True)
#
#     idmovies = models.ForeignKey('Movies', db_column="idmovies", on_delete=models.CASCADE)
#     idactors = models.ForeignKey('Actors', db_column="idactors", on_delete=models.CASCADE)
#
#     class Meta:
#         managed = False
#         db_table = 'acted_in'
#
# class MoviesGenres(models.Model):
#     idmovies_genres = models.AutoField(primary_key=True)
#     idmovies = models.ForeignKey('Movies', db_column="idmovies", on_delete=models.CASCADE)
#     idgenres = models.ForeignKey('Genres', db_column="idgenres", on_delete=models.CASCADE)
#     idseries = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'movies_genres'
