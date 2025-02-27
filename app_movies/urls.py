from django.urls import path,include
from rest_framework.routers import DefaultRouter

from app_movies import views
from app_movies.views import CommentDetail, CommentListApiView, MovieViewSet

app_name = 'movies'


router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path("",views.MovieList.as_view(),name="movie_list"),
    path("<int:pk>/",views.MovieDetail.as_view(),name="movie_detail"),

    path("actor/",views.ActorList.as_view(),name="actor_list"),
    path("actor/<int:pk>/",views.ActorDetail.as_view(),name="actor_detail"),

    path('<int:movie_id>/comments/', CommentListApiView.as_view(), name='movie-comments-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='movie-comments-detail'),
    path('', include(router.urls)),
]