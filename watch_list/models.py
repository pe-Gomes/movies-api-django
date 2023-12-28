from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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

class Review(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    primary_key=True,
    null=False,
    editable=False,
  )
  rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  description = models.CharField(max_length=255, null=True)
  watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.rating} | {self.watchlist.title}"