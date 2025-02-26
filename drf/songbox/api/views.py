from django.shortcuts import render
from api.models import Movie
from rest_framework import serializers

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import MovieSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Movie
from api.serializers import MovieSerializer

class MovieListCreate(APIView):
    def get(self, request,*args,**kwargs):
        movies = Movie.objects.all()
        serializer_instance= MovieSerializer(movies, many=True)
        return Response(serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        data=request.data

        #deserialization
        serializer_instance=MovieSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=201)
        else:
            return Response(serializer_instance.errors,status=400)
        
        


class MovieRetrieveUpdateDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        qs=Movie.objects.get(id=id)

        serializers_instance=MovieSerializer(qs)

        return Response(data=serializers_instance.data)
    



