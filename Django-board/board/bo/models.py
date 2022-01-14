from django.db import models
from django.conf import settings
from hitcount.models import HitCountMixin, HitCount
# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation


class Board(models.Model, HitCountMixin):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, blank=True, null=True)
    ip = models.GenericIPAddressField()
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    hit_count_generifc = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title
