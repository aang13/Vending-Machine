from django.db import models

# Create your models here.

class Vending_machine(models.Model):
    machine_area=models.CharField(max_length=30)
    machine_id=models.IntegerField()

    def __str__(self):
        return '%s %s ' %(self.machine_area,self.machine_id)


class Products(models.Model):
    product_name=models.CharField(max_length=20)
    product_quantity=models.IntegerField()
    per_unit_price=models.IntegerField(default=10)
    vending_machine=models.ForeignKey(Vending_machine,on_delete=models.CASCADE)

    def __str__(self):
        return  '%s %s %s %s' %(self.product_name,self.product_quantity,self.vending_machine,self.per_unit_price)

class Transsactions(models.Model):
    FIVE="5"
    TEN="10"
    TWENTY="20"
    FIFTY="50"
    HUNDRED="100"
    FIVEHUN='500'
    ONETHU="1000"

    INSERTED_AMOUNNT=(
        (FIVE,'5'),
        (TEN,'10'),
        (TWENTY,'20'),
        (FIFTY,'50'),
        (HUNDRED,'100'),
        (FIVEHUN,'500'),
        (ONETHU,'1000')
    )

    inserted_amount=models.CharField(max_length=30,choices=INSERTED_AMOUNNT)
    available_products=models.ManyToManyField(Products)

    def __str__(self):
        return self.INSERTED_AMOUNNT