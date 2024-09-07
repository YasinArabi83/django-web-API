from django.db import models


class CarAds(models.Model):
    code = models.CharField(unique=True)
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    mileage = models.IntegerField()
    location = models.CharField()
    body_color = models.CharField()
    body_type = models.CharField()
    transmission = models.CharField()
    price = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'car_ads'
