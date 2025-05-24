from rest_framework import serializers
from .models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownerfields = '__all__'