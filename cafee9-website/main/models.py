from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='menu/')

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_type = models.CharField(max_length=100)
    date = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return self.name
