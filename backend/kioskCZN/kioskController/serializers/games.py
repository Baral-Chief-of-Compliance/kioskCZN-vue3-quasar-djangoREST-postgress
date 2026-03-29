from rest_framework import serializers

from kioskController.models import GameUrl


class GameSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_name')

    def get_name(self, obj: GameUrl):
        return obj.game.name
    
    class Meta:
        model = GameUrl
        fields = [
            'id',
            'url',
            'pc',
            'game',
            'name'
        ]