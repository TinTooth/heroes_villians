from rest_framework import serializers
from .models import SuperType

class SuperTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id','type']

