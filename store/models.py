from django.db import models

class Collection(models.Model):
    title=models.CharField(max_length=255)

class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT)

class Customer(models.Models):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER="S"
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES= [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD), "Gold"
    ]

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_lenght=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20)
    birthdate=models.DateField(null=True)
    membership=models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

class Item(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Order(models.Model):
    PAYMENT_COMPLETED='C'
    PAYMENT_PENDING='P'
    PAYMENT_FAILED='F'

    PAYMENT_STATUS=[
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETED, 'Completed')
        (PAYMENT_FAILED)
    ]
    placed_at=models.DateTimeField(auto_created=True)
    payment_status=models.CharField(max_length=1, choices=PAYMENT_STATUS)
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    order=models.ForeignKey(Order, on_delete=models.PROTECT)
    quantiy=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
