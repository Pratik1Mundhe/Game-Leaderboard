from leaderboard.interactors.storages.storage_interface import StorageInterface
from leaderboard.models import *
from typing import Optional, List

class StorageImplementation(StorageInterface):
    def create_player(self, user_name: str, password: str) -> Player:
        return Player.objects.create(
            user_name=user_name,
            password=password
        )
    
    def get_existing_user_names(self) -> List[str]:
        return list(Player.objects.all().values_list("user_name", flat=True))
    
    def update_player_details(self, user_id: int, user_name: Optional[str], password: Optional[str]):
        player = Player.objects.filter(id=user_id)
        if not player.exists():
            raise Exception(f"Player with id:{user_id} DoesNotExists")
        
        player = player[0]
        if user_name:
            player.user_name = user_name
        
        if password:
            player.password = password

        player.save()

    def delete_player(self, user_id: str):
        Player.objects.filter(id=user_id).delete()

    def create_game(self, name: str, description: str) -> Game:
        return Game.objects.create(name=name, description=description)

    def get_existing_game_names(self) -> List[str]:
        return list(Game.objects.values_list("name", flat=True))

    def update_game_details(self, game_id: str, name: Optional[str], description: Optional[str]):
        game = Game.objects.filter(id=game_id)

        if not game.exists():
            raise Exception(f"Game with id: {game_id} DoesNotExists")
        
        game = game[0]  
        if name:
            game.name = name
        
        if description:
            game.description = description

        game.save()
        return game
    
    def delete_game(self, game_id: str):
        Game.objects.filter(id=game_id).delete()
    
    def get_games(self, game_ids: List[str]) -> List[Game]:
        return list(Game.objects.filter(id__in=game_ids))


    def validate_game_id(self, game_id: str):
        game = Game.objects.filter(id=game_id)

        if not game.exists():
            raise Exception("Game doesn't exists")
        
    def get_existing_player_ids(self):
        return list(Player.objects.all().values_list("id", flat=True))
    

    def create_game_session(self, game_id: str, start_time: str, end_time: str):
        game_session = Session.objects.create(
            game_id=game_id,
            start_time=start_time,
            end_time=end_time,
        )

        return game_session


    def update_game_session(self, session_id: str,start_time: Optional[str], end_time: Optional[str]):
        game_session = Session.objects.filter(id=session_id)

        if not game_session.exists():
            raise Exception("Session doesn't exists")
        
        game_session = game_session[0]
        if start_time:
            game_session.start_time = start_time

        if end_time:
            game_session.end_time = end_time

        game_session.save()

        return game_session
    

    def delete_game_session(self, session_id: str):
        Session.objects.filter(id=session_id).delete()


    def get_game_session(self, session_id: str):
        session =  Session.objects.filter(id=session_id)
        if not session.exists():
            raise Exception("Session Doesn't Exists")
        
        return session


    def _get_player(self, player_id: str):
        return Player.objects.filter(id=player_id)

    def add_player_to_session(self, session_id: str, player_id: str):
        session = Session.objects.get(id=session_id)
        player = self._get_player(player_id=player_id)
        session.players.add(player) 
        session.save()

    def remove_player_from_session(self, session_id: str, player_id: str):
        session = Session.objects.get(id=session_id)
        player = self._get_player(player_id=player_id)
        session.players.remove(player) 
        session.save()
        
    def validate_session_id(self, session_id: str):
        session = Session.objects.filter(id=session_id)
        if not session.exists():
            raise Exception("Session doesn't exists")

    def validate_player_id(self, player_id: str):
        player = Player.objects.filter(id=player_id)
        if not player.exists():
            raise Exception("Player doesn't exists")
    
