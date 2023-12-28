from django.urls import path

from watch_list.api.views import StreamPlatformListAV, StreamPlatformDetailsAV, WatchListAV, WatchDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<uuid:id>/', WatchDetailsAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-platform-list'),
    path('stream/<uuid:id>', StreamPlatformDetailsAV.as_view(), name='stream-platform-details'),
]