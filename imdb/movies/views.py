from django.shortcuts import render
from .models import Movie
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer, UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse


# Create your views here.
class MovieList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):  #
        serializer.save(owner=self.request.user)

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'movies': reverse('movies', request=request, format=format),
    
        })

