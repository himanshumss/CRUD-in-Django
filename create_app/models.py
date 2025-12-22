from django.db import models

# Create your models here.
class student(models.Model):
    stid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name