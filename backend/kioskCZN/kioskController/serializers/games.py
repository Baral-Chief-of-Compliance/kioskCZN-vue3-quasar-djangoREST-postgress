from rest_framework import serializers

from kioskController.models import GameUrl


class GameSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField('get_name')
    img = serializers.SerializerMethodField('get_img')

    def get_name(self, obj: GameUrl):
        return obj.game.name

    def get_img(self, obj: GameUrl):
        if obj.game.img:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.game.img.url)
        return None
    
    class Meta:
        model = GameUrl
        fields = [
            'id',
            'url',
            'pc',
            'game',
            'name',
            'img'
        ]