from django.db import models

# Create your models here.
# Model from notes
class Post(models.Model):
    # Manually setting the primary key
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140,default='Jonathan') # Added other field
    date = models.DateTimeField()