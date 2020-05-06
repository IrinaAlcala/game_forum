from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import ReviewForm


# Define the home view
def home(request):
  return render(request, 'home.html')

class GameList(ListView):
  model = Game

  def get_queryset(self):
    return Game.objects.all()

# class GameDetail(DetailView):
#   model = Game

def game_detail(request,pk):
  game = Game.objects.get(id=pk)
  review_form = ReviewForm()
  return render(request, 'main_app/game_detail.html', {
    'game' : game,
    'review_form' : review_form
  })

def add_review(request,pk):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.game_id=pk
    new_review.save()

  return redirect('games_detail', pk=pk)


class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games'