from .models import Organization, Manager, Users
from .serializers import OrganizationSerializer, ManagerSerializer, UserSerializer
from rest_framework import viewsets

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objecets.all()
    serializer_class = OrganizationSerializer