from rest_framework import generics
from .models import Genre, Director, Film, Afish
from .serializer import GenreSerialiser, DirectorSerialiser, AfishSerialiser, FilmsSerialiser


class FilmsListCreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerialiser
class FilmsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerialiser


class DirectorListCreateView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerialiser
class DirectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerialiser


class AfishListCreateView(generics.ListCreateAPIView):
    queryset = Afish.objects.all()
    serializer_class = AfishSerialiser
class AfishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Afish.objects.all()
    serializer_class = AfishSerialiser


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerialiser
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerialiser
