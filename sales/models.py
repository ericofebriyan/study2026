from django.db import models
from django.urls import reverse


class Perfume(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.brand})" if self.brand else self.name

    def get_absolute_url(self):
        return reverse('perfume-detail', kwargs={'pk': self.pk})