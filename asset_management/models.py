from django.db import models

# Create your models here.
class Asset(models.Model):
    ASSET_TYPE_CHOICES = (
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        ('television', 'Television')
    )
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPE_CHOICES)
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.asset_type} - {self.serial_number}"