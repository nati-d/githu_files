from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=300)
    completed=models.BooleanField(default=False)
    created=models.DateField (auto_now_add=True)
    updated=models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.task
    
class TestModel(models.Model):  
       name=models.CharField(max_length=300)
       
       def __str__(self) -> str:
        return self.name