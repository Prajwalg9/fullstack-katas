from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.EmailField()
    phone=models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.caption}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    date=models.DateField(auto_now=True)
    text=models.TextField()
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)