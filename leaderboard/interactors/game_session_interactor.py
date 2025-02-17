from typing import Optional, List
from leaderboard.interactors.storages.storage_interface import StorageInterface
from leaderboard.interactors.presenters.presenter_interface import PresenterInterface
from leaderboard.utils import get_date_time_obj, utc_date_time_now
from django.http import JsonResponse
from leaderboard.mixins.validation_mixin import ValidationMixin


class GameSessionInteractor(ValidationMixin):
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_game_session(self, game_id: str, start_time: str, end_time: str):
        self._validate_create_game_session_params(game_id=game_id, start_time=start_time, end_time=end_time)
        game_session = self.storage.create_game_session(game_id=game_id, start_time=start_time, end_time=end_time)
        return self.presenter.prepare_create_game_session_response(game_session=game_session)

    def update_game_session(self,session_id: str, start_time: Optional[str], end_time: Optional[str]):
        self._validate_update_game_session_params(session_id=session_id, start_time=start_time, end_time=end_time)
        game_session = self.storage.update_game_session(session_id=session_id, start_time=start_time, end_time=end_time)
        return self.presenter.prepare_create_game_session_response(game_session=game_session)
    

    def _validate_update_game_session_params(self, session_id: str, start_time: Optional[str], end_time: Optional[str]):
        self.storage.validate_session_id(session_id=session_id)
        self._validate_game_time(session_id=session_id, start_time=start_time, end_time=end_time)
       

    def _validate_create_game_session_params(self, game_id: str, start_time: Optional[str], end_time: Optional[str]):
        self.storage.validate_game_id(game_id=game_id)
        self._validate_game_time(session_id=None, start_time=start_time, end_time=end_time)

    def _validate_player_ids(self, player_ids: List[str]):
        existing_player_ids = self.storage.get_existing_player_ids()
        invalid_player_ids = [player_id for player_id in player_ids if player_id not in existing_player_ids]
        return invalid_player_ids            

 
    def delete_game_session(self, session_id: str):
        self.storage.delete_game_session(session_id=session_id)
        return self.presenter.prepare_delete_game_session_response(session_id=session_id)


    def add_player_to_session(self, session_id: str, player_id: str):
        self._validate_session_and_player(session_id=session_id, player_id=player_id)
        self.storage.add_player_to_session(session_id=session_id, player_id=player_id)
        return JsonResponse({"player_id":player_id})
    
    def remove_player_from_session(self, session_id: str, player_id: str):
        self._validate_session_and_player(session_id=session_id, player_id=player_id)
        self.storage.remove_player_from_session(session_id=session_id, player_id=player_id)
    
    def _validate_session_and_player(self, session_id: str, player_id: str):
        self.storage.validate_session_id(session_id=session_id)
        self.storage.validate_player_id(player_id=player_id)


