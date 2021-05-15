from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# auth imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "signup.html", context)

