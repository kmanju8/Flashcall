from django.db import models

class Card(models.Model):
    front = models.TextField(blank=True, null =True)
    back =  models.CharField(blank=True, null =True, max_length=100)
