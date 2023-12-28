from django.db import models

import uuid

class StreamingPlatform(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    primary_key=True,
    null=False,
    editable=False
  )
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=255)
  url = models.URLField(max_length=200)
  
  def __str__(self):
    return self.name

class WatchList(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    primary_key=True,
    null=False,
    editable=False
  )
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name="watch_list")
  release_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.title