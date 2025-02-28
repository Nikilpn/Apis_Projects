from django.urls import path
from restapp.views import *

urlpatterns=[
    path('register/',Registerview.as_view()),
    path('login/',Loginview.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
]