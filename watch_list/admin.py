from django.contrib import admin
from watch_list.models import WatchList, StreamingPlatform

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamingPlatform)