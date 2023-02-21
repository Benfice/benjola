import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Lesson(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson_detail", kwargs={"pk": self.pk})
    