from django.db import models
from django.conf import settings
# Create your models here.
# from django.contrib.contenttypes.fields import GenericRelation


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, blank=True, null=True)
    ip = models.GenericIPAddressField()
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.title
