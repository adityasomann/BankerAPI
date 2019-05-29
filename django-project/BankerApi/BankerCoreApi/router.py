from BankerCoreApi.viewsets import OrganizationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('BankerCoreApi', OrganizationViewSet)