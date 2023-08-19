from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)           # auto_now=True, this value stores the date and time every time when the object is created or updated in the database
    created = models.DateTimeField(auto_now_add=True)       # auto_now_add=True, this will store the value for only once when the object is created,
    

    def __str__(self):
        return self.body[0:50]