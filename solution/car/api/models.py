from django.db import models

class Car(models.Model):
    trip = models.CharField(null=True, max_length=50)
    refuel = models.CharField(null=True, max_length=50)
    maintenance = models.CharField(null=True, max_length=50)
    create_car = models.CharField(null=True, max_length=50)
    get_car_status = models.CharField(null=True, max_length=50)
    create_tyre = models.CharField(null=True, max_length=50)

    tyres = models.IntegerField(null=True)
    liters = models.IntegerField(null=True)
    total_km = models.IntegerField(null=True)
    disagree = models.IntegerField(null=True)
    piece = models.CharField(null=True, max_length=10)

    def __str__(self):
        return 'Trip'


    class Meta:
        db_table = 'car'