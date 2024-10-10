from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from app.dbmodels.models import Player, Game, Shot, Team
from .serializers import PlayerSummarySerializer

class PlayerSummary(APIView):
    def get(self, request, player_id):
        player = get_object_or_404(Player, id=player_id)  # Get player or return 404 if not found
        serializer = PlayerSummarySerializer(player)  # Use the nested serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
