from django.contrib import admin
from watch_list.models import WatchList, StreamingPlatform, Review

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamingPlatform)
admin.site.register(Review)