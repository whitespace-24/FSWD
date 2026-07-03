from django.db import models

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User

class Bounty(models.Model):
    target_name = models.CharField(max_length=200)
    reward = models.IntegerField()
    status = models.CharField(max_length=50, default="wanted")
    
    # The owner is tied to the User who created it
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.target_name