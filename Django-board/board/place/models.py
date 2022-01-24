from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=200)
    count = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self) -> str:
        return self.location_name


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100)
    place_info = models.CharField(max_length=50)
    place_review_score = models.CharField(max_length=30, null=True)
    place_review_visit = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    place_review_blog = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    place_location = models.CharField(max_length=100, blank=True, null=True)
    place_subway = models.CharField(max_length=100, blank=True, null=True)
    place_time = models.CharField(max_length=1000, blank=True, null=True)
    place_imageurl = models.URLField(max_length=500, blank=True, null=True)
    place_register = models.DateTimeField(null=True)
    location = models.ForeignKey(
        Location, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.place_name
