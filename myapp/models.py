from django.db import models

# Create your models here.

class Product_mst(models.Model):
    Product_Name = models.CharField(max_length=100)
    def __str__(self) -> str:
           return self.Product_Name
class Product_sub_cat(models.Model):
    Product_prize = models.IntegerField()
    Product_img = models.FileField(upload_to="product_images", default='flower.jpg')
    Product_model = models.CharField(max_length=150)
    Product_ram = models.CharField(max_length=50)
    Product_name =  models.ForeignKey(Product_mst, on_delete=models.CASCADE)
    def __str__(self) -> str:
           return self.Product_ram