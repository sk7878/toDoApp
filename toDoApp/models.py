from django.db import models
from django.shortcuts import reverse


# Create your models here.
class ToDoModel(models.Model):
    title = models.CharField(max_length=20)
    detail = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/update/{self.id}"
        # return reverse("todo:update", kwargs={'pk': self.id})

