from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game



# Define the home view
def home(request):
  return render(request, 'home.html')

class GameList(ListView):
  model = Game

  def get_queryset(self):
    return Game.objects.all()

class GameDetail(DetailView):
  model = Game

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games'