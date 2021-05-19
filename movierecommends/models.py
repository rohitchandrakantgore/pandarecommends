from django.db import models

# Create your models here.

class MovieData(models.Model):
    rank = models.TextField()
    movie_name = models.CharField(max_length=150, unique=True)
    poster = models.URLField()
    year = models.IntegerField()
    streamOn = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name