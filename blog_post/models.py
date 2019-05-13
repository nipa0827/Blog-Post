from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

class Student(models.Model):
	name = models.CharField(max_length=20)
	roll = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
	student_class = models.CharField(max_length=20)


