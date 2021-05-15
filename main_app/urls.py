
from django.urls import path
from .views import Signup
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', Signup.as_view(), name="signup"),

]
