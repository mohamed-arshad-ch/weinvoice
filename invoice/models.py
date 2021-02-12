from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False)
    hsn = models.CharField(max_length=150,blank=True,null=True)
    price = models.FloatField(blank=False,null=False)
    stock = models.IntegerField(blank=False,null=False)
    store_id = models.CharField(max_length=150,blank=False,null=False)
    unit = models.CharField(max_length=150,blank=False,null=False)

    def __str__(self):
        return self.name