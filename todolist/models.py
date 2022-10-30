from django.db import models
from django.utils import timezone
from django.urls import reverse





class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    date = models.DateTimeField(default=timezone.now())
    due_time = models.DateTimeField(default=timezone.now())
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


   

    
   