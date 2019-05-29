
from django.urls import path
from .views import ListSongsView, ArtistView, OrganiationListView


urlpatterns = [
    path('songs/getsongs', ListSongsView.as_view(), name="songs-all"),
    path('artists/', ArtistView.as_view(), name="artist-all"),
    path('organizations/GetOrganizations', OrganiationListView.as_view(), name="organization-all")
]