"""
All models here must be registered in admin.py
Anytime a change is made here must run:
1. 'python manage.py makemigrations'
2. 'python manage.py migrate'
^^This will ensure that things don't break if you change a field, etc.
"""
from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
