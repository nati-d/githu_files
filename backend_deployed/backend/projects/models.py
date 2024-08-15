from django.db import models
from api.models  import *
import logging
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    team= models.ForeignKey(Team, on_delete=models.CASCADE,null=True)
   
    def __str__(self) -> str:
         project_name = self.project_name if self.project_name else 'Unnamed Project'
         print(project_name)
         return project_name

    