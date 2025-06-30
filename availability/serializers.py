from rest_framework import serializers
from .models import WeeklyAvailability

# Yeh serializer model ko JSON me convert karta hai (aur JSON se model bhi)
class WeeklyAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        # Kaunse model ke liye serializer bana rahe hain
        model = WeeklyAvailability

        # Kaunse fields ko API me include karna hai — '__all__' ka matlab sabhi fields
        fields = '__all__'
