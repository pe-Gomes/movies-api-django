from django.urls import path

from watch_list.api.views import (StreamPlatformListAV,
                                  StreamPlatformDetailsAV,
                                  WatchListAV,
                                  ReviewList,
                                  ReviewPerMovie,
                                  WatchDetailsAV,
                                  ReviewDetails)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<uuid:id>/', WatchDetailsAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-platform-list'),
    path('stream/<uuid:id>', StreamPlatformDetailsAV.as_view(), name='stream-platform-details'),
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<uuid:pk>', ReviewDetails.as_view(), name='review-details'),
    path('<uuid:pk>/review', ReviewPerMovie.as_view(), name='reviews-per-movie')
]