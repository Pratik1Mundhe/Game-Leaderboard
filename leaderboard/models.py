from django.db import models

# Create your models here.
class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="Sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    upvotes = models.IntegerField(default=0)
    players = models.ManyToManyField("Player")