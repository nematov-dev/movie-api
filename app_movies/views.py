from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app_movies.models import Movie, Actor, Comment
from app_movies.permissions import IsAdminOrReadOnly, IsAdminOwnerOrReadOnly
from app_movies.serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOrReadOnly]
     queryset = Movie.objects.all()
     serializer_class = MovieSerializer

class ActorList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOrReadOnly]
     queryset = Actor.objects.all()
     serializer_class = ActorSerializer

class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        return Comment.objects.filter(movie_id=movie_id)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOwnerOrReadOnly,IsAuthenticated]
     serializer_class = CommentSerializer

     def get_queryset(self):
         movie_id = self.kwargs.get('movie_id')
         comment_id = self.kwargs.get('pk')

         return Comment.objects.filter(id=comment_id,movie_id=movie_id)

