from django.db import models
from django.utils import timezone


class Post(models.Model):
    __current_time = timezone.now()
    content = models.TextField()
    enabled = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    unpublished_date = models.DateTimeField(default=None, null=True)

    def is_published(self):
        now = timezone.now()
        return self.enabled == True and self.published_date < now < self.unpublished_date

