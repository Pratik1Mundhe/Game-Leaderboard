"""
URL configuration for game_leaderboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    # path("", views.index, name="index")
    path("player/create/", views.create_player, name="create player"),
    path("player/update/", views.update_player, name="update player"),
    path("player/delete/", views.delete_player, name="delete player"),
    path("game/create/", views.create_game, name="create game"),
    path("game/update/", views.update_game, name="update game"),
    path("game/delete/", views.delete_game, name="delete game"),
    path("game_session/create/", views.create_game_session, name="create game session"),
    path("game_session/update/", views.update_game_session, name="delete game session"),
    path("game_session/delete/", views.delete_game_session, name="delete game session"),
    path("game_session/add_player/", views.add_player_to_session, name="add player to session"),
    path("game_session/delete_player/", views.remove_player_from_session, name="remove player from session"),
]
