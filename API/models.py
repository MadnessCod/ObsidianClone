import os

from django.db import models


# Create your models here.


class MyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    def __str__(self):
        return NotImplemented("str method not implemented")


class File(MyBaseModel):
    name = models.CharField(max_length=64)
    file = models.FileField(upload_to="files/")

    def save(self, *args, **kwargs):
        if self.file:
            self.name = os.path.basename(self.file.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.file.name
