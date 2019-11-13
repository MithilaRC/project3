from django.db import models

# Create your models here.
class CosmeticsTypeModel(models.Model):
    c_typeno = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=100)

class CosmeticsModel(models.Model):
    c_no = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=100)
    c_price = models.FloatField()
    c_type = models.ForeignKey(CosmeticsTypeModel, on_delete=models.CASCADE)