from django.db import models

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()

    class Meta:
        db_table = 'products'
