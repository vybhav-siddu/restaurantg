from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    price=models.DecimalField(max_digits=20,decimal_places=3)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price=models.DecimalField(max_digits=20,decimal_places=3)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.CharField(max_length=500)

    def __int__(self):
        return self.table_number()

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_number = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=500)
    contact_number=models.IntegerField()
    

    def __str__(self):
        return self.name
