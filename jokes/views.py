from django.shortcuts import render

from django.views.generic import DetailView, ListView
from .models import Joke

# Create your views here.
class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke