from rest_framework import serializers

from api.models import RoastBoast

class RoastBoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoastBoast
        fields = [
            'roastorboast',
            'post',
            'upvotes',
            'downvotes',
            'time',
            'id'
        ]