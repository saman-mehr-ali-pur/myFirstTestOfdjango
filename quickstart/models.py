from django.db import models
from django.core.validators import RegexValidator



class Passenger(models.Model):
    firstName = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100,null=False )
    birthdate = models.DateField(null=False)
    email = models.EmailField(max_length=100,null=True)
    phone = models.CharField(validators=[RegexValidator(r'^09.{9}$',"invalid phone number")],default="")
    nationalCode = models.CharField(max_length=10,validators=[
            RegexValidator(r'^.{10}$', 'Code must contain exactly 10 characters.')
        ],
        db_index=True)

    
class AirLine(models.Model):
    name=models.CharField(max_length=50)



class Country(models.Model):
    name = models.CharField(max_length=100,unique=True)



class City(models.Model):
    name = models.CharField(max_length=100,unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=False)



class AirPort(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)


class Fligth(models.Model):

    startingPoint = models.ForeignKey(City,on_delete=models.CASCADE,null=False)
    destination = models.CharField(max_length=100)
    AirPort = models.ForeignKey(AirPort,on_delete=models.CASCADE)
    serial = models.CharField(max_length=100)
    flightDate = models.DateField(null=False)


