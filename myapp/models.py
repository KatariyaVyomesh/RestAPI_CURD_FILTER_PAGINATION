from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('EC', 'Electronics and Communication'),
        ('OTHER', 'Other'),
    ]


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default='OTHER')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
