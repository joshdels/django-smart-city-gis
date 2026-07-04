from django.contrib.gis.db import models as gis_models
from django.db import models

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

