from rest_framework.decorators import APIView
from rest_framework.response import Response

from watch_list.models import WatchList, StreamingPlatform
from watch_list.api.serializers import WatchListSerializer, StreamingPlatformSerializer

# Create your views here.
class WatchListAV(APIView):
  def get(self, request):
    items = WatchList.objects.all()
    serialization = WatchListSerializer(items, many=True)
    return Response(serialization.data)
  
  def post(sefl, request):
    serialization = WatchListSerializer(data=request.data)
    if serialization.is_valid():
      serialization.save()
      return Response(serialization.data, status=201)
    else:
      return Response(serialization.errors, status=500)
  
class WatchDetailsAV(APIView):
  def get(self, request, id):
    try:
      item = WatchList.objects.get(id=id)
    except WatchList.DoesNotExist:
      return Response(status=404)
      
    serialization = WatchListSerializer(item)
    return Response(serialization.data)
    
  def delete(self, request, id):
    try:  
      item = WatchList.objects.get(id=id)
    except WatchList.DoesNotExist:
      return Response(status=404)
    
    item.delete()
    return Response(status=204)


class StreamPlatformListAV(APIView):
  def get(self, request):
    platform = StreamingPlatform.objects.all()
    serialization = StreamingPlatformSerializer(platform, many=True)
    return Response(serialization.data, status=200)
  
  def post(self, request):
    serialization = StreamingPlatformSerializer(data=request.data)
    if serialization.is_valid():
      serialization.create()
      return Response(serialization.data, status=201)
    else:
      return Response(serialization.errors, status=500)
  
class StreamPlatformDetailsAV(APIView):
  def get(self, request, id):
    try:
      item = StreamingPlatform.objects.get(id=id)
    except StreamingPlatform.DoesNotExist:
      return Response(status=404)
    
    serialization = StreamingPlatformSerializer(item)
    return Response(serialization.data)
  
  