from leaderboard.interactors.presenters.presenter_interface import PresenterInterface
from django.http import JsonResponse
from typing import Optional, List
from leaderboard.models import *
class PresenterImplementation(PresenterInterface):
    def prepare_update_player_response(self, user_id: int, user_name: str):
        response = {
            "user_id" : user_id,
            "user_name": user_name
        }

        return JsonResponse(response)
    
    def prepare_delete_player_response(self, user_id: int):
        response = {"user_id" : user_id}
        return JsonResponse(response)
    
    @staticmethod
    def _prepare_game_response(game: Game):
        return {
            "id" : game.id,
            "name": game.name,
            "description" : game.description
        }
    
    def prepare_create_game_response(self, game: Game):
        response = self._prepare_game_response(game=game)
        return JsonResponse(response)
    
    def prepare_delete_game_response(self, game_id: str):
        response = {"game_id": game_id}
        return JsonResponse(response)
    
    def prepare_create_game_session_response(self, game_session: Session):
        response = self._prepare_game_session_response(game_session=game_session)
        return JsonResponse(response)
    
    def prepare_delete_game_session_response(self, session_id: str):
        response = {"session_id": session_id}
        return JsonResponse(response)
    
    def _prepare_game_session_response(self, game_session: Session):
        return {
            "id": game_session.id,
            "game_id": game_session.game_id,
            "start_time": game_session.start_time,
            "end_time": game_session.end_time,
            "upvotes": game_session.upvotes
        }