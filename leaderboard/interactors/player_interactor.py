from typing import Optional
from leaderboard.interactors.storages.storage_interface import StorageInterface
from django.shortcuts import HttpResponse
from leaderboard.interactors.presenters.presenter_interface import PresenterInterface


class PlayerInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_player(self, user_name: str, password: str):
        self._validate_user_name(user_name=user_name)
        pid = self.storage.create_player(user_name=user_name, password=password)
        return HttpResponse(pid)

    def _validate_user_name(self, user_name: str):
        user_names = self.storage.get_existing_user_names()

        if user_name in user_names:
            raise Exception("Username Already Exists")

    def update_player(self, user_id: int, user_name: Optional[str], password: Optional[str]):
        if user_name:
            self._validate_user_name(user_name=user_name)
        
        self.storage.update_player_details(user_id=user_id, user_name=user_name, password=password)

        return self.presenter.prepare_update_player_response(user_id=user_id, user_name=user_name)

    def delete_player(self, user_id: str):
        self.storage.delete_player(user_id=user_id)

        return self.presenter.prepare_delete_player_response(user_id=user_id)


    def get_players(self, game_id: Optional[str]):
        if game_id:
            players = self.storage.get_players(game_id=game_id)
        else:
            players = self.storage.get_all_players()

        return self.presenter.prepare_get_players_response(players=players)
        


