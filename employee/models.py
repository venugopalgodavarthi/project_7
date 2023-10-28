from django.db import models

# Create your models here.


class employee_m(models.Model):
    eid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.PositiveBigIntegerField(unique=True)
    salary = models.PositiveIntegerField(null=True)
    age = models.PositiveSmallIntegerField(null=True, default=18)
    address = models.TextField()
    doj = models.DateField()
    dom = models.DateTimeField(auto_now=True)
