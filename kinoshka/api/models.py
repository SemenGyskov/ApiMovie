from django.db import models

class Director(models.Model):
    FIO = models.CharField(max_length=150)
    datebirtch = models.DateField()

class Genre(models.Model):
    name = models.CharField(max_length=40)

class Film(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    country = models.CharField(max_length=40)
    director = models.ManyToManyField(Director, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)

class Afish(models.Model):
    date = models.DateField()
    film = models.ManyToManyField(Film)