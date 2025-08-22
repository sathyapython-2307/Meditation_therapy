from django.db import models
from django.contrib.auth.models import User

class Approach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    therapy_days = models.CharField(max_length=10)
    family_count = models.IntegerField()
    address = models.TextField()
    time_availability = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
