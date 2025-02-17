from django.contrib import admin
from leaderboard.models import *
# Register your models here.


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "password"]

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ["id", "game_id", "start_time", "end_time", "upvotes"]