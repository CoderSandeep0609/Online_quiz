from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20,blank=False)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(choices=[('','Choose Gender'),('male','male'),('female','female'),('others','others')],blank=False)
    age=models.IntegerField(blank=False)
    qualification=models.CharField(choices=[
        ('','Choose Qualification'),
        ('matriculation','matriculation'),
        ('intermediate','intermediate'),
        ('Diplaoma','Diplaoma'),
        ('Gaduation','Gaduation'),
        ('Master Degree','Master Degree'),
    ],blank=False)
    marks=models.IntegerField(blank=False)


class ExamData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(blank=False)
    marks_obtained=models.IntegerField(blank=False)
    total_marks=models.IntegerField(blank=False)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

