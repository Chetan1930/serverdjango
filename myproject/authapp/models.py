from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='todos')
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
