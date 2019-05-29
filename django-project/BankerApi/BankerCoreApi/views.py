from rest_framework import generics
from .models import Manager, Users, Organization
from .serializers import ManagerSerializer, UserSerializer, OrganizationSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ArtistView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class OrganiationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer