from typing import Optional, List
from leaderboard.interactors.storages.storage_interface import StorageInterface
from django.shortcuts import HttpResponse
from leaderboard.interactors.presenters.presenter_interface import PresenterInterface

class GameInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_game(self, name: str, description: str):
        self._validate_game_name(name)
        game = self.storage.create_game(name=name, description=description)
        return self.presenter.prepare_create_game_response(game=game)

    def _validate_game_name(self, name: str):
        existing_names = self.storage.get_existing_game_names()
        if name in existing_names:
            raise Exception("Game Name Already Exists")

    def update_game(self, game_id: str, name: Optional[str], description: Optional[str]):
        if name:
            self._validate_game_name(name)  
        game = self.storage.update_game_details(game_id=game_id, name=name, description=description)
        return self.presenter.prepare_create_game_response(game=game)

    def delete_game(self, game_id: str):
        self.storage.delete_game(game_id=game_id)
        return self.presenter.prepare_delete_game_response(game_id=game_id)

    def get_games(self, game_ids: List[str]):
        games = self.storage.get_games(game_ids=game_ids)
        return self.presenter.prepare_get_games_response(games=games)
