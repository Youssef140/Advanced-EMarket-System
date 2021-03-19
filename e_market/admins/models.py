from django.db import models
from datetime import datetime

#tuples of the dropdown options
position_choices = (
    ('manager','Manager'),
    ('staff','Staff'),
    ('cashier','Cashier')
)

class Admin(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    position = models.TextField(blank=False,choices=position_choices)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    entry_date = models.DateTimeField(default=datetime.now)

    #definition of what a record should be named
    def __str__(self):
        return self.first_name+" "+self.middle_name+" "+self.last_name