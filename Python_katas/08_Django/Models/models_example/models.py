from django.db import models
from django.utils import timezone

class Employee(models.Model):
    Specialization=[
        ("Ai","Ai Engineer"),
        ("Data","Data Scientist"),
        ("Fron","FrontEnd Developer"),
        ("Back","BackEnd Developer"),
        ("Anyl","Data Analyst"),
    ]
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    profession=models.CharField(max_length=4, choices=Specialization)
    date=models.DateTimeField(default=timezone.now)
    profile_picture=models.ImageField(upload_to='profile_picture')
