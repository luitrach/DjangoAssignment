from django.db import models

class Employees(models.Model):
    Name = models.CharField(max_length= 20)
    Contact = models.IntegerField()
    Address = models.CharField(max_length= 30)

    def __str__(self):
        return self.Name