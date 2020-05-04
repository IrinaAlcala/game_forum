from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('games/', views.games_index, name='index'),
  path('games/<int:game_id>/', views.games_detail, name='detail'),
]