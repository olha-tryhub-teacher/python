from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Столик {self.number} ({self.seats} місць)"


class Booking(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="reservations"
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    guests_count = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "start_time"]
        unique_together = ("table", "date", "start_time")

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")

    def __str__(self):
        return f"{self.date} {self.start_time} — Table {self.table.number}"