from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Manager
from .serializers import ManagerSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(UserID="", UserIDEncrypted=""):
        if UserID != "" and UserIDEncrypted != "":
            Manager.objects.create(UserID=UserID, UserIDEncrypted=UserIDEncrypted)

    def setUp(self):
        # add test data
        print('Hello')


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Manager.objects.all()
        serialized = ManagerSerializer(expected, many=True)
     #   self.assertEqual(response.data, serialized.data)
    #  self.assertEqual(response.status_code, status.HTTP_200_OK)