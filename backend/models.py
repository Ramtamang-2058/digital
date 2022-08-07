from django.db import models


Locations=(
    ("Kathmandu","Kathmandu"),
    ("Dolakha","Dolakha"),
    ("Lalitpur","Lalitpur"),
    ("Teku","Teku"),
    ("Bhaktapur","Bhaktapur"),
    ("Hetauda","Hetauda")


)

class Trainer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=40)
    education=models.CharField(max_length=40)
    organization=models.CharField(max_length=40)


class Registration(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    college =models.CharField(max_length=40)
    education =models.CharField(max_length=40)
    district =models.CharField(max_length=30)
    training_location =models.CharField(choices=Locations,default = 'Kathmandu', max_length=30)
    age =models.PositiveIntegerField(null=True, blank=True)
    phone =models.CharField(max_length=10)
    email =models.EmailField()
    interest =models.CharField(max_length=30)
    basic_skill=models.CharField(max_length=30)
    date=models.DateField()
    time=models.DateTimeField()


class Attendes(models.Model):
    id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=30)
    college=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email =models.EmailField()
    address =models.CharField(max_length=30)
    training_location =models.CharField(choices=Locations,default = 'Kathmandu', max_length=30)
    interest =models.TextField()
    basic_skill=models.TextField()
    date=models.DateField()
    time=models.DateTimeField()


class Events(models.Model):
    Location =models.CharField(max_length=30)
    image =models.ImageField()
    description =models.TextField()
    title =models.CharField(max_length=30)
    date=models.DateField()
    time =models.DateTimeField()

