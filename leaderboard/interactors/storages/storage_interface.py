from abc import ABC, abstractmethod
from typing import List, Optional
from leaderboard.models import *

class StorageInterface(ABC):
    @abstractmethod
    def create_player(self, user_name: str, password: str) -> Player:
        pass

    @abstractmethod
    def get_existing_user_names(self) -> List[str]:
        pass

    @abstractmethod
    def update_player_details(self, user_id: int, user_name: Optional[str], password: Optional[str]):
        pass

    @abstractmethod
    def delete_player(self, user_id: str):
        pass

    @abstractmethod
    def create_game(self, name: str, description: str) -> Game:
        pass

    @abstractmethod
    def get_existing_game_names(self) -> List[str]:
        pass

    @abstractmethod
    def update_game_details(self, game_id: str, name: Optional[str], description: Optional[str]):
        pass

    @abstractmethod
    def delete_game(self, game_id: str):
        pass
    
    @abstractmethod
    def get_games(self, game_ids: List[str]) -> List[Game]:
        pass

    @abstractmethod
    def create_game_session(self, game_id: str, start_time: str, end_time: str):
        pass

    @abstractmethod
    def update_game_session(self, session_id: str,start_time: Optional[str], end_time: Optional[str]):
        pass

    @abstractmethod
    def delete_game_session(self, session_id: str):
        pass

    @abstractmethod
    def validate_game_id(self, game_id: str):
        pass

    @abstractmethod
    def get_existing_player_ids(self):
        pass

    @abstractmethod
    def get_game_session(self, session_id: str):
        pass

    @abstractmethod
    def add_player_to_session(self, session_id: str, player_id: str):
        pass

    @abstractmethod
    def remove_player_from_session(self, session_id: str, player_id: str):
        pass

    @abstractmethod
    def validate_session_id(self, session_id: str):
        pass

    @abstractmethod
    def validate_player_id(self, session_id: str, player_id: str):
        pass
