
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api/v1/tasks',views.TaskViewSetView,basename="tasks")

urlpatterns = [

]+router.urls