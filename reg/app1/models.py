from django.db import models

class Crud(models.Model):
    username=models.CharField(unique=True, max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


