from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length = 100,blank = True,null = True)
    date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.task

