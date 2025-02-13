from django.db import models

# Create your models here.

class Room(models.Model):
    Room =[
        ('single','single'),
        ('Double','Double'),
        ('SUITE','suite'),
    ]
class  Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=15,unique=True)

class Booking(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out=models.DateField()
    total_price=models.DecimalField(max_digits=10,decimal_places=2)

class Booking(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)


