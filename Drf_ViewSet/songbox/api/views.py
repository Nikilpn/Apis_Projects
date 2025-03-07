from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from api.models import Movie
from rest_framework import serializers

# Create your views here.



from rest_framework.response import Response
from api.serializers import MovieSerializer


from rest_framework.response import Response



from rest_framework import status


from rest_framework.viewsets import ViewSet
class MovieViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        serializer_instance=MovieSerializer(qs,many=True)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        data=request.data
        serializer_instance=MovieSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(qs)
        return Response(data=serializer_instance.data)
    def update(self,request,*args,**kwargs):
        data=request.data
        id=kwargs.get("pk")
        movie_object=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(data=data,instance=movie_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance,status=status.HTTP_404_NOT_FOUND)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id)
        return Response(data={"message":"delete"})