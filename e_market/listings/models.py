from django.db import models
from datetime import datetime
from admins.models import Admin

#tuples of the dropdown options
currency_choices = (
    ('usd','USD'),
    ('lbp','LBP')
)

cat_id = 1

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_categ_id = models.ForeignKey('Category',default='Category',on_delete=models.DO_NOTHING,blank=True,null=True)
    # cat_id=cat_id+1
    is_child = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name




class Product(models.Model):
    admin = models.ForeignKey(Admin,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    currency = models.CharField(max_length=10,choices=currency_choices,default='usd')
    brand_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    in_stock = models.BooleanField()
    # class_id = models.ForeignKey(Class)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.title



