from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import Task
from api.serializers import TaskSerializer,UserSerializer

from rest_framework import authentication,permissions

from api.serializers import UserSerializer
from rest_framework import serializers


class TaskViewSetView(ViewSet):
    authentication_classes = [authentication.BasicAuthentication]#setting authentication
    permission_classes = [permissions.IsAuthenticated]#setting permission

    def list(self,request,*args,**kwargs):
        qs=Task.objects.filter(user_object=request.user)
        serializer_instance=TaskSerializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        data=request.data

        serializer_instance=TaskSerializer(data=data)

        if serializer_instance.is_valid():
            serializer_instance.save(user_object=request.user)#for modelserializer
            #Task.objects.create(**serializer_instance.validated_data)#for normalserializer
        
            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,*args,**kwargs): 

    
        id=kwargs.get("pk")
        
        qs=Task.objects.get(id=id)

        if qs.user_object!=request.user:
            raise serializers.ValidationError("permisssion denied")


        serializer_instance=TaskSerializer(qs)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        task_object=Task.objects.get(id=id)
        if request.user!=task_object.user_object:
            raise serializers.ValidationError("permission denied")
        serializer_instance=TaskSerializer(data=request.data,instance=task_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Task.objects.get(id=id)
        if request.user!=task_object.user_object:
            raise serializers.ValidationError("permission denied")
        try:
            Task.objects.get(id=id).delete()
            return Response(data={"message":"deleted"},status=status.HTTP_200_OK)
        except:
            return Response(data={"message":"resorce not found"},status=status.HTTP_404_NOT_FOUND)
        
class UserView(APIView):
    def post(self,request,*args,**kwargs):
        
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

        
