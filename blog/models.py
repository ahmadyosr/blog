from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class BlogPost(models.Model):
	post_title=models.CharField(max_length=200)
	post_text=models.CharField(max_length=200)
	post_length=models.IntegerField(default=0)
	post_date=models.DateTimeField(default=datetime.now())


