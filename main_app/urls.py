
from django.urls import path

# Add Profile below in future
from .views import Signup, Home
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('accounts/profile/', Profile.as_view(), name="profile"),
    path('accounts/pub_profile/', views.PubProfile.as_view(), name="pub_profile"),
    path('accounts/signup/', Signup.as_view(), name="signup"),
    # path('', views.showslides),

]

# path('accounts/', include(django.contrib.auth.urls')),
