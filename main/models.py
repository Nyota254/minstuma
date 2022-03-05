from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    '''
    This class will contain students model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    notes = models.TextField(null=True,blank=True)
    course_complete = models.BooleanField(default=False)
    enrollment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        This dunda method makes it easier to read
        '''
        return f"{self.first_name} {self.second_name}"

    class Meta:
        '''
        Ordering to be based on whether a student has completed the course
        '''
        ordering = ['course_complete']
