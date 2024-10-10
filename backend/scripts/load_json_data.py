import json
import os
from app.dbmodels.models import Player, Game, Shot, Team
from django.conf import settings

players_file_path = os.path.join(settings.BASE_DIR, 'raw_data', 'players.json')
games_file_path = os.path.join(settings.BASE_DIR, 'raw_data', 'games.json')
teams_file_path = os.path.join(settings.BASE_DIR, 'raw_data', 'teams.json')

def load_player_data():
    with open(players_file_path, 'r') as file:
        data = json.load(file)
        players = [Player(id=item['id'], name=item['name']) for item in data]
        Player.objects.bulk_create(players, ignore_conflicts=True)
    print("Player data loaded successfully!")

def load_team_data():
    with open(teams_file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            Team.objects.get_or_create(id=item['id'], defaults={'name': item['name']})
    print("Team data loaded successfully!")

def load_game_data():
    with open(games_file_path, 'r') as file:
        data = json.load(file)
        for game_data in data:
            for player_data in game_data['homeTeam']['players']:
                player = Player.objects.get(id=player_data['id'])
                game, created = Game.objects.get_or_create(
                    player=player,
                    date=game_data['date'],
                    defaults={
                        'is_starter': player_data['isStarter'],
                        'minutes': player_data['minutes'],
                        'points': player_data['points'],
                        'assists': player_data['assists'],
                        'offensive_rebounds': player_data['offensiveRebounds'],
                        'defensive_rebounds': player_data['defensiveRebounds'],
                        'steals': player_data['steals'],
                        'blocks': player_data['blocks'],
                        'turnovers': player_data['turnovers'],
                        'defensive_fouls': player_data['defensiveFouls'],
                        'offensive_fouls': player_data['offensiveFouls'],
                        'free_throws_made': player_data['freeThrowsMade'],
                        'free_throws_attempted': player_data['freeThrowsAttempted'],
                        'two_pointers_made': player_data['twoPointersMade'],
                        'two_pointers_attempted': player_data['twoPointersAttempted'],
                        'three_pointers_made': player_data['threePointersMade'],
                        'three_pointers_attempted': player_data['threePointersAttempted'],
                    }
                )

                for shot_data in player_data['shots']:
                    Shot.objects.get_or_create(
                        game=game,
                        is_make=shot_data['isMake'],
                        location_x=shot_data['locationX'],
                        location_y=shot_data['locationY']
                    )
    print("Game and Shot data loaded successfully!")

def load_data():
    load_player_data()
    load_team_data()
    load_game_data()
    print("All data loaded successfully!")

load_data()
