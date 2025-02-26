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

from rest_framework import status


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
        try:

            qs=Movie.objects.get(id=id)

            serializers_instance=MovieSerializer(qs)

            return Response(data=serializers_instance.data)
        except:
            context={"message":"requested resorces not found"}

            return Response(data=context,status=status.HTTP_404_NOT_FOUND)
    

    def delete(self,request,*args,**kwargs):

    
        id=kwargs.get("pk")

        try:
            Movie.objects.get(id=id).delete()

            return Response(data={"message":"deleted"},status=status.HTTP_200_OK)
        except:

            return Response(data={"message":"resource not found"},status=status.HTTP_404_NOT_FOUND)
        

    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=request.data

        movie_object=Movie.objects.get(id=id)

        serializer_instance=MovieSerializer(data=data,instance=movie_object) #instance is used for updating
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=200)
        else:
            return Response(serializer_instance.errors,status=400)

    



