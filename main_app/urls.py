
from django.urls import path

# Add Profile below in future
from .views import Signup, Home
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('accounts/profile/', Profile.as_view(), name="profile"),
    path('accounts/pub_profile/', views.PubProfile.as_view(), name="pub_profile"),
    path('accounts/signup/', Signup.as_view(), name="signup"),

    path('pub_profile/', views.PubProfile.as_view(), name="pub_profile"),

    path('', views.showslides),

    path('pub_profile/<int:pk>/', views.PostDetail.as_view(), name="post_detail")

]

# path('accounts/', include(django.contrib.auth.urls')),
