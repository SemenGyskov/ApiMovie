from rest_framework import serializers
from .models import Afish, Film, Genre, Director

class FilmsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'date', 'country','director','genre']

class AfishSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Afish
        fields = ['id','date', 'film']

class GenreSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']

class DirectorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'FIO','datebirtch']
