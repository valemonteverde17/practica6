from rest_framework import serializers
from .models import Comida, Bebida, Snack 

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'
        
class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebida
        fields = '__all__'
        
class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = '__all__'