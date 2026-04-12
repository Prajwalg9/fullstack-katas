from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVaraity(models.Model):
    chai_type=[
        ('MS','Masala Tea'),
        ('GR','Ginger Tea'),
        ('PL','Plain Tea')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=chai_type)
    description =models.TextField(default="")
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    chai=models.ForeignKey(ChaiVaraity,on_delete=models.CASCADE,related_name="reviews")
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField()
    date_added=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user.username} review for {self.chai}'

class Stores(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varaity=models.ManyToManyField(ChaiVaraity,related_name='stores')
    
    def __str__(self):
        return self.name


class Certificate (models.Model):
    chai=models.OneToOneField(ChaiVaraity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=5)
    issued_date=models.DateField(default=timezone.localdate)
    valid_till=models.DateField()
    
    def __str__(self):
        return f"Certificate for {self.chai}"
    

