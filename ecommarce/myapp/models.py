from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
