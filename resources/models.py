import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Resource(models.Model):
    ENGLISH = 'EN'
    FRANCAIS = 'FR'
    SRPSKI = 'SR'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'Anglais'),
        (FRANCAIS, 'Français'),
        (SRPSKI, 'Serbe'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resource_detail", kwargs={'pk' : self.pk})
    