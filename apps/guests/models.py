from django.db import models


class Guest(models.Model):
    organization = models.CharField(max_length=255, blank=True, default="Individual")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    inquiry = models.TextField()
    phone = models.CharField(max_length=30, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.organization} ({self.email})"
