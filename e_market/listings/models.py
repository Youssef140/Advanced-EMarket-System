from django.db import models
from datetime import datetime
from admins.models import Admin
from django.contrib.auth.models import User
import os
from uuid import uuid4
from datetime import datetime
from django.db import models



#tuples of the dropdown options
currency_choices = (
    ('usd','USD'),
    ('lbp','LBP')
)

cat_id = 1

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_categ_id = models.ForeignKey('Category',default='Category',on_delete=models.DO_NOTHING,blank=True,null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_child = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    description = models.TextField(blank=True,null=True)
    def _str_(self):
        return self.name




class Product(models.Model):
    admin = models.ForeignKey(Admin,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
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
    is_offer = models.BooleanField(default=False,blank=True,null=True)
    # valid_until = models.DateTimeField(default=datetime.now,blank=True)
    def _str_(self):
        return self.title


    @property
    def imageURL(self):
        try:
            url = self.photo_main.url
        except:
            url = ''
            return url



class SearchImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    search_image = models.ImageField(null=True,blank=True,upload_to="images/")



class UserSearchedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    searched_image = models.ImageField(null=True,blank=True,upload_to='searched_images/')




def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper




currency_choices = (
    ('usd', 'USD'),
    ('lbp', 'LBP')
)


