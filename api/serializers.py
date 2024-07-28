from rest_framework import serializers
from krishnart.models import Drawings

class DrawingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawings
        fields = '__all__'
        