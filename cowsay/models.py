from django.db import models
from django.utils import timezone

# Create your models here.


class CowSentence(models.Model):
    cow_text = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cow_text
