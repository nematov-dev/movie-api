from django.urls import path

from app_movies import views
from app_movies.views import CommentDetail, CommentListApiView

app_name = 'movies'

urlpatterns = [
    path("",views.MovieList.as_view(),name="movie_list"),
    path("<int:pk>/",views.MovieDetail.as_view(),name="movie_detail"),

    path("actor/",views.ActorList.as_view(),name="actor_list"),
    path("actor/<int:pk>/",views.ActorDetail.as_view(),name="actor_detail"),

    path('<int:movie_id>/comments/', CommentListApiView.as_view(), name='movie-comments-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='movie-comments-detail'),
]