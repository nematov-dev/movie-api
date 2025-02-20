from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    imdb = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    genre = models.CharField(max_length=50, )
    actor = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Actor(models.Model):
    gender = (
        ('m', 'man'),
        ('w', 'woman'),
    )

    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=gender, default='man')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
