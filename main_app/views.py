from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game
from .forms import ReviewForm


# Define the home view
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'genre', 'description', 'publisher']
  success_url = '/games/'
  
  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['name', 'genre', 'description', 'publisher']
  success_url = '/games/'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'


def home(request):
  return render(request, 'home.html')

@login_required
def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  review_form = ReviewForm()
  return render(request, 'games/detail.html', {
    'game': game,
    'review_form': review_form,
  })

@login_required
def add_review(request, game_id):
  form = ReviewForm(request.POST, request.FILES)

  if form.is_valid():
    # here are the changes with Fred!
    new_review = form.save(commit=False)
    new_review.game_id = game_id
    new_review.name_id = request.user.id
    new_review.save()

  return redirect('detail', game_id=game_id)

class GameList(LoginRequiredMixin, ListView):
    model = Game

    def get_queryset(self):
      return Game.objects.filter(user=self.request.user)
