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

    def __str__(self):
        return self.full_name

class Order(models.Model):
    client_id = models.IntegerField()
    car_model = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car_model} - {self.service.name} - {self.master.full_name}"
