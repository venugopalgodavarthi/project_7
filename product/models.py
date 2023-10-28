from django.db import models

# Create your models here.


class product_model(models.Model):
    pid = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=60)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
