from django.db import models
from job.models import Job
# Create your models here.
from django.contrib.auth.models import User

class Candidate(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,default='Male')
    age=models.IntegerField()
    mobile=models.IntegerField()
    city=models.CharField(max_length=50)
    exp_salary=models.IntegerField()
    will_relocate=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class CandidateJobMap(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job=models.ForeignKey('job.Job',on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='pending')
    def __str__(self):
        return f"{self.candidate.name} {self.job.position_name}"