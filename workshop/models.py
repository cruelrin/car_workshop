from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Master(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

class Order(models.Model):
    car_model = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    hours_worked = models.IntegerField(default=0)

    @property
    def total_price(self):
        return self.master.price_per_hour * self.hours_worked

    def __str__(self):
        return f"Order #{self.id} - {self.car_model}"
