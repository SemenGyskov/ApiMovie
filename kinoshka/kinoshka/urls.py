
from django.contrib import admin
from django.urls import path
from api.views import FilmsListCreateView, FilmsRetrieveUpdateDestroyView, DirectorListCreateView, DirectorRetrieveUpdateDestroyView, AfishListCreateView, AfishRetrieveUpdateDestroyView, GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', FilmsListCreateView.as_view(), name='films-list-create'),
    path('films/<int:pk>/', FilmsRetrieveUpdateDestroyView.as_view(), name='films-retrieve-update-destroy'),
    path('director/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('director/<int:pk>/', DirectorRetrieveUpdateDestroyView.as_view(), name='director-retrieve-update-destroy'),
    path('afish/', AfishListCreateView.as_view(), name='afish-list-create'),
    path('afish/<int:pk>/', AfishRetrieveUpdateDestroyView.as_view(), name='afish-retrieve-update-destroy'),
    path('genre/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genre/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy'),



]
