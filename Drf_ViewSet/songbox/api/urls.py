from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register("api/v1/movies", views.MovieViewSetView, basename="movies") 

urlpatterns = [
  
]+router.urls
