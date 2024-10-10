from rest_framework import serializers
from app.dbmodels.models import Player, Game, Shot

class ShotSerializer(serializers.ModelSerializer):
    isMake = serializers.BooleanField(source='is_make')
    locationX = serializers.FloatField(source='location_x')
    locationY = serializers.FloatField(source='location_y')

    class Meta:
        model = Shot
        fields = ['isMake', 'locationX', 'locationY']

class GameSerializer(serializers.ModelSerializer):
    isStarter = serializers.BooleanField(source='is_starter')
    freeThrowsMade = serializers.IntegerField(source='free_throws_made')
    freeThrowsAttempted = serializers.IntegerField(source='free_throws_attempted')
    twoPointersMade = serializers.IntegerField(source='two_pointers_made')
    twoPointersAttempted = serializers.IntegerField(source='two_pointers_attempted')
    threePointersMade = serializers.IntegerField(source='three_pointers_made')
    threePointersAttempted = serializers.IntegerField(source='three_pointers_attempted')
    offensiveRebounds = serializers.IntegerField(source='offensive_rebounds')
    defensiveRebounds = serializers.IntegerField(source='defensive_rebounds')
    defensiveFouls = serializers.IntegerField(source='defensive_fouls')
    offensiveFouls = serializers.IntegerField(source='offensive_fouls')
    shots = ShotSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            'date', 'isStarter', 'minutes', 'points', 'assists',
            'offensiveRebounds', 'defensiveRebounds', 'steals', 'blocks',
            'turnovers', 'defensiveFouls', 'offensiveFouls', 'freeThrowsMade',
            'freeThrowsAttempted', 'twoPointersMade', 'twoPointersAttempted',
            'threePointersMade', 'threePointersAttempted', 'shots'
        ]

class PlayerSummarySerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['name', 'games']
