from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    
    def __str__(self):
        return self.name