from django.shortcuts import render

from quickstart.models import Passenger
from rest_framework import permissions, viewsets

from quickstart.serializers import PassengerSerializer


class PassngerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Passenger.objects.all().order_by("lastName")
    serializer_class = PassengerSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """

#     queryset = Group.objects.all().order_by("name")
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]