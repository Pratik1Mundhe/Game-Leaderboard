from leaderboard.interactors.player_interactor import PlayerInteractor
from leaderboard.storages.storage_implementation import StorageImplementation
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import HttpResponse
from leaderboard.presenters.presenter_implementation import PresenterImplementation
from leaderboard.interactors.game_interactor import GameInteractor
from leaderboard.interactors.game_session_interactor import GameSessionInteractor

@csrf_exempt
def create_player(request):
    body = json.loads(request.body)
    user_name = body["user_name"]
    password = body["password"]
    interactor = PlayerInteractor(
        storage=StorageImplementation(),
        presenter=PresenterImplementation()
    )

    try:
        response = interactor.create_player(
            user_name=user_name,
            password=password
        )
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response

@csrf_exempt
def update_player(request):
    body = json.loads(request.body)
    user_id = body["user_id"]
    user_name = body["user_name"]
    password = body["password"]

    interactor = PlayerInteractor(
        storage=StorageImplementation(),
        presenter=PresenterImplementation()
    )

    try:
        response = interactor.update_player(
            user_id=user_id,
            user_name=user_name,
            password=password
        )
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response

@csrf_exempt
def delete_player(request):
    body = json.loads(request.body)
    user_id = body["user_id"]

    interactor = PlayerInteractor(
        storage=StorageImplementation(),
        presenter=PresenterImplementation()
    )

    try: 
        response = interactor.delete_player(
            user_id=user_id,
        )
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response


@csrf_exempt
def create_game(request):
    body = json.loads(request.body)
    name = body["name"]
    description = body["description"]
    
    interactor = GameInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.create_game(name=name, description=description)
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response

@csrf_exempt
def update_game(request):
    body = json.loads(request.body)
    game_id = body["game_id"]
    name = body.get("name")  # Optional
    description = body.get("description")  # Optional
    
    interactor = GameInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.update_game(game_id=game_id,name=name, description=description)
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response

@csrf_exempt
def delete_game(request):
    body = json.loads(request.body)
    game_id = body["game_id"]
    interactor = GameInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.delete_game(game_id=game_id)
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response

@csrf_exempt
def create_game_session(request):
    body = json.loads(request.body)
    game_id = body["game_id"]
    start_time = body["start_time"]
    end_time = body["end_time"]

    interactor = GameSessionInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.create_game_session(
            game_id=game_id,
            start_time=start_time,
            end_time=end_time
        )
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response


@csrf_exempt
def update_game_session(request):
    body = json.loads(request.body)
    session_id = body["session_id"]
    start_time = body.get("start_time")  # Optional
    end_time = body.get("end_time")  # Optional

    interactor = GameSessionInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.update_game_session(
            session_id=session_id,
            start_time=start_time,
            end_time=end_time
        )
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response


@csrf_exempt
def delete_game_session(request):
    body = json.loads(request.body)
    game_id = body["game_id"]

    interactor = GameSessionInteractor(storage=StorageImplementation(), presenter=PresenterImplementation())

    try:
        response = interactor.delete_game_session(game_id=game_id)
    except Exception as err:
        return HttpResponse(f"error: {str(err)}")

    return response


@csrf_exempt
def add_player_to_session(request):
    pass

@csrf_exempt
def remove_player_from_session(request):
    pass

@csrf_exempt
def upvote_game_session(request):
    pass

@csrf_exempt
def get_players(request):
    pass

@csrf_exempt
def get_games(request, level):
    pass
