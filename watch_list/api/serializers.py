from rest_framework import serializers

from watch_list.models import WatchList, StreamingPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
  reviews = ReviewSerializer(many=True, read_only=True)
  
  class Meta:
    model = WatchList
    fields = "__all__"

class StreamingPlatformSerializer(serializers.ModelSerializer):
  #watch_list = WatchListSerializer(many=True ,read_only=True)
  #watch_list = serializers.StringRelatedField(many=True)
  watch_list = serializers.PrimaryKeyRelatedField(many=True ,read_only=True)
  
  class Meta:
    model = StreamingPlatform
    fields = "__all__"
    