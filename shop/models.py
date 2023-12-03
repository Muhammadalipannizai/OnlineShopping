from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    categary=models.CharField(max_length=500,default='')
    subcategary=models.CharField(max_length=500,default='')
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=60)
    desc=models.CharField(max_length=400)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    con_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=600)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=3000)
    amount=models.IntegerField(default=0)
    order_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.order_name


class OrderUpdate(models.Model):
     update_id = models.AutoField(primary_key=True)
     order_id = models.IntegerField(default="")
     update_desc = models.CharField( max_length=5000)
     timestamp = models.DateField(auto_now_add=True)

     def __str__(self):
        return self.update_desc[0:7]+ " ...."
