from django.db import models

class categories(models.Model):
    img = models.ImageField( upload_to='image')
    cat_name = models.CharField(max_length = 1000)
    link = models.CharField(max_length=1000,default="category-")

class items(models.Model):
    img = models.ImageField(upload_to = "image")
    item_name = models.CharField(max_length=1000)
    item_type = models.CharField(max_length = 1000)
    category = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_des = models.CharField(max_length=1000)
    offer = models.BooleanField(default=False)
    top_add = models.BooleanField(default=False)
    our_special = models.BooleanField(default=False)


class add_cart(models.Model):
    img = models.ImageField(upload_to = "image")
    item_name = models.CharField(max_length=1000)
    item_type = models.CharField(max_length = 1000)
    category = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_des = models.CharField(max_length=1000)
    quantity = models.IntegerField(default="1")
    user = models.CharField(max_length=1000,default="none")
    offer = models.BooleanField(default=False)
    top_add = models.BooleanField(default=False)
    our_special = models.BooleanField(default=False)


class temp_cart(models.Model):
    img = models.ImageField(upload_to = "image")
    item_name = models.CharField(max_length=1000)
    item_type = models.CharField(max_length = 1000)
    category = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_des = models.CharField(max_length=1000)
    quantity = models.IntegerField(default="1")
    user = models.CharField(max_length=1000,default="none")
    offer = models.BooleanField(default=False)
    top_add = models.BooleanField(default=False)
    our_special = models.BooleanField(default=False)



from django.contrib.auth.models import User
from django.db import models

        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)