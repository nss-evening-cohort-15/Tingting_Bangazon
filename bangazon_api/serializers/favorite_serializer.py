from rest_framework import serializers
from bangazon_api.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('customer', 'store')
        depth = 1
