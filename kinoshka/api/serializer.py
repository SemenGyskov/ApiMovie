from rest_framework import serializers
from .models import Afish, Film, Genre, Director

class FilmsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class AfishSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Afish
        fields = '__all__'

class GenreSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class DirectorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
