from django.contrib.gis.db import models as gis_models
from django.db import models


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)

    status = models.CharField(max_length=100, default="active")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Parcels(models.Model):
    parcel_id = models.CharField(max_length=200, unique=True)

    geom = gis_models.PolygonField(srid=4326)

    ownership = models.ForeignKey(
        Owner, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels"
    )

    status = models.CharField(max_length=100)
    paid_status = models.BooleanField(default=False)


class Boundary(models.Model):
    region_name = models.CharField(max_length=255)
    province_name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    barangay_name = models.CharField(max_length=255)

    region_code = models.CharField(max_length=50, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    barangay_code = models.CharField(max_length=50, blank=True, null=True)

    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f"{self.barangay_name}, {self.city_name}, {self.province_name}, {self.region_name}"
