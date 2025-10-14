from django.shortcuts import render # type: ignore
from django.views.generic.list import ListView # type: ignore
from taskorg.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

# Create your views here.
