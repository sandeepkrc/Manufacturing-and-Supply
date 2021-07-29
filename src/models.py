from django.db import models
from django.db import models




class BussinessCustomer(models.Model):
    bcid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=200)
    cemail = models.EmailField(max_length=254)
    cadd = models.CharField(max_length=200)
    pwd = models.CharField(max_length=20)
    cpwd = models.CharField(max_length=20)




class Product(models.Model):
    id = models.IntegerField(primary_key=True)   #PRIMARY KEY USED
    pname= models.CharField(max_length=200)
    pcost = models.DecimalField(max_digits=10,decimal_places=4)
    pmfd = models.DateField(auto_now_add=True)
    pexpd = models.DateField()
    quantity = models.CharField(max_length=225)


    def __str__(self):
        return self.pname















class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)   #ForeignKey USED
    sid = models.IntegerField()  #supplier id
    bcid = models.IntegerField()   #ALSO WANT TO  RELATE WITH Bussiness TABLE



class Supplier(models.Model):

    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=200)
    scompany = models.CharField(max_length=200)

    #SOME DOUBT want to take from product table and relate with product table
    # product_id = models.OneToOneField(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname




# Create your models here.
