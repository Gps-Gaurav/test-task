from django.db import models
from shared.models import User

# Guest booking detail store karta hai
class Booking(models.Model):
    guest_name = models.CharField(max_length=100)  # Guest ka naam
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kis user ke liye booking hai
    date = models.DateField()  # Booking kis date ki hai
    start_time = models.TimeField()  # Start time
    end_time = models.TimeField()  # End time

    class Meta:
        # Same user, date aur time slot repeat na ho
        unique_together = ('user', 'date', 'start_time', 'end_time')
