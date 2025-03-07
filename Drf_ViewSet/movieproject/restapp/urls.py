
from django.urls import path,include
from restapp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v1/movies",views.MovieViewSetView,basename="movies")

urlpatterns = [




]+router.urls
