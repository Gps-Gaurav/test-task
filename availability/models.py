from django.db import models
from shared.models import User  # Custom User model import kiya gaya hai

class WeeklyAvailability(models.Model):
    # Kis user ne availability set ki — agar user delete ho jaye to uski availability bhi delete ho jayegi
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Week ke kis din ke liye yeh slot hai (0 = Monday, 6 = Sunday)
    day_of_week = models.IntegerField(
        choices=[(i, i) for i in range(7)]  # Choices bana rahe hain dropdown ke liye
    )

    # Kis samay se user available hai
    start_time = models.TimeField()

    # Kis samay tak user available hai
    end_time = models.TimeField()

    class Meta:
        # Ek user same din same time slot ko dobara add na kar sake
        unique_together = ('user', 'day_of_week', 'start_time', 'end_time')
