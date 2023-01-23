import uuid
from django.contrib.auth import get_user_model
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
    teaser_picture = models.ImageField(upload_to="teaser_pictures/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can see all resources"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resource_detail", kwargs={'pk' : self.pk})
    

class Comment(models.Model):
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment