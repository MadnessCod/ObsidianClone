from django.db import models


# Create your models here.

class MyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']

    def __str__(self):
        return NotImplemented('str method not implemented')


class File(MyBaseModel):
    file = models.FileField(upload_to='files/')

    def  __str__(self):
        return self.file.name

    class Meta:
        ordering = ['-updated_at']
