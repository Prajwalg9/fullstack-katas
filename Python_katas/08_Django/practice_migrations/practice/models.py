from django.db import models


# Create your models here.

class Student(models.Model):
    roll_no=models.IntegerField()
    f_name=models.CharField("100")
    l_name=models.CharField("100")
    course=models.CharField("100")
    admission_date=models.TimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.roll_no+self.f_name+self.l_name
    
    
class BCS(models.Model):
    roll_no=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.CharField("100")
    