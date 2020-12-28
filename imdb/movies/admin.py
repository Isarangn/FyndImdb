from django.contrib import admin

from .models import Movie, Genre

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'popularity','director']
    list_filter = ['genre']
    search_fields = ['name', 'director']
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

