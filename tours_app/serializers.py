from rest_framework import serializers
from tours_app.models import Tour


class TourSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Tour
        fields = [
            'id',
            'name',
            'duration',
            'maxGroupSize',
            'difficulty',
            'ratings',
            'price',
            'description'
        ]
