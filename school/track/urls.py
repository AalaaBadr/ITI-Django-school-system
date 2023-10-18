from django.urls import path

from .views import *

urlpatterns = [
    # path('list', list_tracks, name='list_tracks'),
    # path('list', ListTracks.as_view(), name='list_tracks'),
    path('list',ListTrack.as_view(), name='list.tracks'),
    # path('add', add_track, name='add_track'),
    # path('add', AddTrack.as_view(), name='add_track'),
    path('add', add, name='add.track'),
    path('update/<int:id>', update_track, name='update_track'),
    # path('delete/<int:id>', delete_track, name='delete_track'),
    path('delete/(<pk>)', DeleteTrack.as_view(), name='delete.track'),
]
