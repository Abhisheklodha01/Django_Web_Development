from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


# one to many relationship
class ChaiReviews(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many relationship 
class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="chai_stores")  

    def __str__(self):
        return self.name
    

# one to one relationship 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE ,related_name="certificate")
    certficate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
    