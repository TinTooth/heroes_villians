from rest_framework import serializers
from .models import Super
from super_types.models import SuperType


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id','name','alter_ego','primary_ability','secondary_ability','super_type','super_type_id']
        depth = 1

    super_type_id = serializers.IntegerField(write_only = True)

    