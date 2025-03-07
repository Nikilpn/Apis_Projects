from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from api.models import Movie
from django.templatetags.i18n import language
from rest_framework import serializers

# Create your views here.



from rest_framework.response import Response
from api.serializers import MovieSerializer


from rest_framework.response import Response



from rest_framework import status
from rest_framework.views import APIView


from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action


# localhost:8000/api/v1/movies/


class MovieViewSetView(ViewSet):
    # method=get
    def list(self,request,*args,**kwargs):
        #localhost:8000/api/movies?language=value
        qs=Movie.objects.all()

        if 'language' in request.query_params:
            value=request.query_params.get('language')
            qs=qs.filter(language=value)

            # localhost:8000/api/movies?genre=value
        if 'genre' in request.query_params:
            value=request.query_params.get('genre')
            qs=qs.filter(genre=value)


        serializer_instance=MovieSerializer(qs,many=True)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        # method=post
        data=request.data
        serializer_instance=MovieSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,*args,**kwargs):
        # method=get
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(qs)
        return Response(data=serializer_instance.data)
    def update(self,request,*args,**kwargs):
        # method=put
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
        # method=delete
        id=kwargs.get("pk")
        Movie.objects.get(id=id)
        return Response(data={"message":"delete"})


    # #localhost:8000/api/v1/movies/genres
    # method=get
    # no id is passing through url
    @action(methods=["get"],detail=False)
    def genres(self,request,*args,**kwargs):
        qs=Movie.objects.values_list("genre",flat=True).distinct()
        return Response(data=qs)
    #localhost:8000/api/v1/movies/genres
    # method=get
    # no id is passing through url
    @action(methods=["get"],detail=False)
    def languages(self,request,*args,**kwargs):

        qs = Movie.objects.values_list("language", flat=True).distinct()
        return Response(data=qs)

#localhost:8000/api/movies/genres/
#method:get
# class GenreListView(APIView):
#     def get(self,request,*args,**kwargs):

#         qs=Movie.objects.all().values_list("genre",flat=True).distinct()

#         return Response(data=qs)

