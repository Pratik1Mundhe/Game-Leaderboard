from typing import Optional, List   
from leaderboard.models import *

class PresenterInterface:
    def prepare_update_player_response(self, user_id: int, user_name: str):
        pass

    def prepare_delete_player_response(self, user_id: int):
        pass

    def prepare_create_game_response(self, game: Game):
        pass

    def prepare_delete_game_response(self, game_id: str):
        pass

    def prepare_get_games_response(self, games: List[dict]):
        pass

    def prepare_create_game_session_response(self, game_session: Session):
        pass

    def prepare_delete_game_session_response(self, session_id: str):
        pass

    def prepare_get_games_response(self, games: List[dict]):
        pass