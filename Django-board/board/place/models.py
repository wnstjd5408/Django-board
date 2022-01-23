from django.db import models

# Create your models here.


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100)
    place_info = models.CharField(max_length=50)
    place_review_score = models.CharField(max_length=30)
    place_review_visit = models.IntegerField()
    place_review_blog = models.IntegerField()
    place_location = models.CharField(max_length=100, blank=True, null=True)
    place_subway = models.CharField(max_length=100, blank=True, null=True)
    place_time = models.CharField(max_length=300, blank=True, null=True)
    place_imageurl = models.URLField(blank=True, null=True)
    place_register = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.place_name
