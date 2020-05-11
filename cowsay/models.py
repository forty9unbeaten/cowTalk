from django.db import models

# Create your models here.


class TextString(models.Model):
    text = models.CharField(max_length=150)
