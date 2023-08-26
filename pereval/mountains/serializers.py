from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'