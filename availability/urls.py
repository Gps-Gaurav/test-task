from django.urls import path
from .views import WeeklyAvailabilityView

urlpatterns = [
    path('', WeeklyAvailabilityView.as_view(), name='availability'),
]
