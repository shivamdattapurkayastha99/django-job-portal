from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    position_name=models.CharField(max_length=50)
    text_description=models.TextField()
    max_age=models.IntegerField()
    min_age=models.IntegerField()
    salary=models.IntegerField()
    n_openings=models.IntegerField()
    creater=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.position_name
         
