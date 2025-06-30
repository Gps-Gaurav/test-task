from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

# Booking list aur create ke liye view
class BookingCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()  # Sab bookings fetch hongi (for GET)
    serializer_class = BookingSerializer  # Serializer handle karega validation aur save
