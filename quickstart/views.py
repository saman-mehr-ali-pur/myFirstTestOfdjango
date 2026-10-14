from django.shortcuts import render

from .quickstart.models import Passnger
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import PassngerSerializer


class PassngerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Passnger.objects.all().order_by("fisrtName")
    serializer_class = PassngerSerializer
    # permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """

#     queryset = Group.objects.all().order_by("name")
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]