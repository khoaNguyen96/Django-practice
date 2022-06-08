
from django.shortcuts import redirect, render
from .models import Week, Choice
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

def index(request):
    last_week_poll = Week.objects.get(pk=1)
    context = {
        "name": request.user,
        "week_poll": last_week_poll
    }
    return render(request, "index.html", context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def logout_request(request):
    logout(request)
    return redirect("index")

class DetailsView(LoginRequiredMixin, DetailView):
    model = Week
    template_name = "detail.html"

class ResultsView(LoginRequiredMixin, DetailView):
    model = Week
    template_name= "results.html"

def vote(request, week_id):
    try:
        week = Week.objects.get(pk=week_id)
        selected_choice = week.choice_set.get(pk=request.POST["choice"])
    except Week.DoesNotExist:
        raise Http404("Poll for said week does not exists")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect("results", week_id)