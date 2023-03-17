from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=200)
    picture = ImageField(
        'Picture',
        upload_to='pictures/',
        blank=True,
    )
    def __str__(self):
        return self.name
    