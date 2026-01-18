from django.db import models
from django.utils import timezone
from datetime import timedelta

class Show(models.Model):
    movie_name = models.CharField(max_length=100)
    show_time = models.DateTimeField(default=timezone.now)
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie_name} at {self.show_time}"
    
class Seat(models.Model):
    AVAILABLE = 'available'
    HELD = 'held'
    BOOKED = 'booked'

    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (HELD, 'Held'),
        (BOOKED, 'Booked'),
    ]

    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=AVAILABLE)
    held_until = models.DateTimeField(null=True, blank=True)

    def is_hold_expired(self):
        return self.status == self.HELD and self.held_until < timezone.now
     
    def __str__(self):
        return f"{self.show} - Seat{self.seat_number}"