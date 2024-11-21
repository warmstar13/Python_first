from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Individual_Post(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text[:50]}..."