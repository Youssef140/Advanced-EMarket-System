from django.db import models
from datetime import datetime
from admins.model import Admin

class Product(models.Model):
    admin = models.ForeignKey(Admin,on_delete=models.DO_NOTHING())
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.deletion)
    price = models.DecimalField(decimal_places=2)
    brand_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    currency = models.CharField(max_length=10)
    in_stock = models.BooleanField()
    class_id = models.ForeignKey(Class)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    rating = models.IntegerField()
    def __str__(self):
        return self.title