from django.shortcuts import render
from .models import Game

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def game_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })