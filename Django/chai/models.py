from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPES_CHOICE = [
        ('ML', "MASALA"),
        ('GR', "GINGER"),
        ('KL', "KIWI"),
        ('PL', "PLAIN"),
        ("EL", "ELACHI")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    added_date = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CHAI_TYPES_CHOICE)
    description = models.TextField(default='')
    price = models.IntegerField(default=50)

    def __str__(self):
        return self.name


