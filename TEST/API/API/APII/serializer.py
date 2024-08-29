from rest_framework import serializers
from app_1.models import Json 

class Jsonserializer(serializers.ModelSerializer):
    class Meta:
        model = Json
        fields = '__all__'