from django.contrib import admin

from app_movies.models import Movie, Comment,Actor

admin.site.register([Movie,Comment,Actor])
