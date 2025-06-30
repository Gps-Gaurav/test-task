from rest_framework import serializers
from .models import Booking
from availability.models import WeeklyAvailability
import datetime

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Sare fields include kiye gaye hain

    def validate(self, data):
        user = data['user']
        date = data['date']
        start = data['start_time']
        end = data['end_time']

        # Booking ka duration nikal rahe hain
        duration = (datetime.datetime.combine(datetime.date.today(), end) -
                    datetime.datetime.combine(datetime.date.today(), start))

        # Sirf allowed durations hi valid hain
        allowed_durations = [datetime.timedelta(minutes=m) for m in [15, 30, 45, 60]]
        if duration not in allowed_durations:
            raise serializers.ValidationError("Duration must be 15, 30, 45, or 60 minutes.")

        # Week ka din nikal rahe hain (0 = Monday)
        day = date.weekday()

        # Check: availability me ye slot exist karta hai ya nahi
        available = WeeklyAvailability.objects.filter(
            user=user,
            day_of_week=day,
            start_time__lte=start,
            end_time__gte=end
        ).exists()

        if not available:
            raise serializers.ValidationError("Not in available timings.")

        # Check: ye slot kisi existing booking se overlap to nahi ho raha
        overlapping = Booking.objects.filter(
            user=user,
            date=date,
            start_time__lt=end,
            end_time__gt=start
        ).exists()

        if overlapping:
            raise serializers.ValidationError("Overlapping with another booking.")

        return data  # Agar sab valid hai to data return karo
