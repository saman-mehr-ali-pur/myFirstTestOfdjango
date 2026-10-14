from .quickstart.models import Passnger
from rest_framework import serializers


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passnger
        fields = ["fistName", "lastName", "email"]


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ["url", "name"]