from rest_framework import generics, permissions
from .models import WeeklyAvailability
from .serializers import WeeklyAvailabilitySerializer

# User apni weekly availability dekh aur add kar sakta hai
class WeeklyAvailabilityView(generics.ListCreateAPIView):
    serializer_class = WeeklyAvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    # Sirf current user ke slots fetch karo
    def get_queryset(self):
        return WeeklyAvailability.objects.filter(user=self.request.user)

    # Slot create karte waqt user field auto set ho
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
