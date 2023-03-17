from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Pictures(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    picture = ImageField(
        'Picture',
        upload_to='pictures/',
        blank=True,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.name
    