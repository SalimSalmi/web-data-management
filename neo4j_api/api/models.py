# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom, Relationship)

class Actor(StructuredNode):
    idactors = UniqueIdProperty()
    lname = StringProperty()
    fname = StringProperty()
    mname = StringProperty()
    gender = IntegerProperty()
    number = IntegerProperty()

    movies = Relationship(
        'Movie','ACTED_IN')

class Genre(StructuredNode):
    idgenres = UniqueIdProperty()
    genre = StringProperty()

    movies = Relationship(
        'Movie','IN_GENRE')


class Movie(StructuredNode):
    idmovies = UniqueIdProperty()
    title = StringProperty()
    year = StringProperty()
    number = IntegerProperty()
    type = StringProperty()
    location = StringProperty()
    language = StringProperty()

    actors = Relationship(
        'Actor', 'ACTED_IN')

    genres = Relationship(
        'Genre', 'IN_GENRE')
