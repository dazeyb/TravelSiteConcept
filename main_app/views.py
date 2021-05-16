from typing import ContextManager
from main_app.models import Post
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# forms, commenting out for migrations
# from .forms import SignUpForm

# auth imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

# This functions but doesn't have extra fields we need, keeping as a backup

# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {"form": form}
#         return render(request, "signup.html", context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("login")
#         else:
#             context = {"form": form}
#             print(form.errors, "Failed to sign-up user")
#             return render(request, "signup.html", context)

class Signup(View):
    def get(self, request):

# Set back to usercreationform for migrations
        form = UserCreationForm
        # form = SignUpForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
        else:
            context = {"form": form}
            print(form.errors, "Failed to sign-up user")
            return render(request, "signup.html", context)



def showslides(request):
    return render(request, 'home.html')

class PubProfile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context



class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
