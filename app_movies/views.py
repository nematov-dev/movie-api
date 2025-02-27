from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app_movies.models import Movie, Actor, Comment
from app_movies.permissions import IsAdminOrReadOnly
from app_movies.serializers import MovieSerializer, ActorSerializer, CommentSerializer

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['post'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')

        try:
            actor = Actor.objects.get(id=actor_id)
            movie.actors.add(actor)
            return Response({'status': 'actor added'})
        except Actor.DoesNotExist:
            return Response({'status': 'actor not found'}, status=404)

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


class CommentListApiView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, movie_id):
        comments = Comment.objects.filter(movie__id=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request, movie_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            movie = Movie.objects.get(id=movie_id)
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAdminOrReadOnly,IsAuthenticated]
     serializer_class = CommentSerializer

     def get_queryset(self):
         comment_id = self.kwargs.get('pk')
         return Comment.objects.filter(id=comment_id)

