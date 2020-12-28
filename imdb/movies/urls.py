from django.urls import path

from .views import UserList, UserDetail, MovieList, MovieDetail, ApiRoot
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import MovieListView

urlpatterns = [
    path('', ApiRoot.as_view(), name = 'root'),
    path('users/', UserList.as_view(), name = 'users'),
    path('users/<int:pk>', UserDetail.as_view(), name = 'single-user'),
    path('movies/', MovieList.as_view(), name = 'movies'),
    path('movies/<int:pk>', MovieDetail.as_view(), name = 'single-movie'),
    
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)