# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ActedIn(models.Model):
    idacted_in = models.AutoField(primary_key=True)
    idmovies = models.IntegerField()
    idseries = models.IntegerField(blank=True, null=True)
    idactors = models.IntegerField()
    character = models.CharField(max_length=2047, blank=True, null=True)
    billing_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acted_in'


class Actors(models.Model):
    idactors = models.IntegerField(primary_key=True)
    lname = models.CharField(max_length=1023, blank=True, null=True)
    fname = models.CharField(max_length=1023, blank=True, null=True)
    mname = models.CharField(max_length=1023, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actors'


class AkaNames(models.Model):
    idaka_names = models.AutoField(primary_key=True)
    idactors = models.IntegerField()
    name = models.CharField(max_length=1023, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aka_names'


class AkaTitles(models.Model):
    idaka_titles = models.AutoField(primary_key=True)
    idmovies = models.IntegerField()
    title = models.CharField(max_length=1023, blank=True, null=True)
    location = models.CharField(max_length=63, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aka_titles'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genres(models.Model):
    idgenres = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class Keywords(models.Model):
    idkeywords = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'


class Movies(models.Model):
    idmovies = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1023, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=63, blank=True, null=True)
    language = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class MoviesGenres(models.Model):
    idmovies_genres = models.AutoField(primary_key=True)
    idmovies = models.IntegerField()
    idgenres = models.IntegerField()
    idseries = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_genres'


class MoviesKeywords(models.Model):
    idmovies_keywords = models.AutoField(primary_key=True)
    idmovies = models.IntegerField()
    idkeywords = models.IntegerField()
    idseries = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies_keywords'


class Series(models.Model):
    idseries = models.IntegerField(primary_key=True)
    idmovies = models.IntegerField()
    name = models.CharField(max_length=1023, blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'
