from django.contrib.gis.db import models as gis_models
from django.db import models

from apps.accounts import models as accounts_model


class Owner(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    date_owned = models.DateField(blank=True, null=True)

    status = models.CharField(max_length=100, default="active")
    created_at = models.DateField(auto_now_add=True)


class TaxInformation(models.Model):
    tax_declaration = models.CharField(max_length=255)
    tax_payment_status = models.CharField(
        max_length=100,
    )

    market_value = models.FloatField(blank=True, null=True)
    classification = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=100, default="active")
    created_at = models.DateField(auto_now_add=True)


class Parcel(gis_models.Model):
    external_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_index=True,
    )

    parcel_id = models.CharField(max_length=200, blank=True, null=True)
    area_auto_m2 = models.FloatField(blank=True, null=True)
    area_declared = models.FloatField(blank=True, null=True)
    barangay_name = models.CharField(max_length=255, blank=True, null=True)

    geom = gis_models.MultiPolygonField(srid=4326)

    ownership = models.ForeignKey(
        Owner, on_delete=models.SET_NULL, null=True, blank=True, related_name="parcels"
    )

    tax_information = models.ForeignKey(
        TaxInformation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parcels",
    )

    user = models.ForeignKey(
        accounts_model.User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parcels",
    )

    status = models.CharField(max_length=100, default="active", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
