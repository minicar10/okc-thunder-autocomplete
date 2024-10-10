from django.db import models

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games')
    date = models.DateField()
    is_starter = models.BooleanField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensive_fouls = models.IntegerField()
    offensive_fouls = models.IntegerField()
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    two_pointers_made = models.IntegerField()
    two_pointers_attempted = models.IntegerField()
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()

class Shot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='shots')
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
