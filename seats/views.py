from django.db import transaction
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from .models import Seat, Show

@transaction.atomic
def hold_seats(request, show_id):
    seat_numbers = request.GET.getlist('seats')
    hold_minutes = 5

    seats = (
        Seat.objects
        .select_for_update()
        .filter(show_id=show_id, seat_number__in=seat_numbers)
    )

    for seat in seats:
        if seat.status != Seat.AVAILABLE:
            return JsonResponse({"error": "One or more seats are not available."}, status=400)
        
    for seat in seats:
        seat.status = Seat.HELD
        seat.held_untill = timezone.now() + timedelta(minutes=hold_minutes)
        seat.save()

    return JsonResponse({"message": "Seats held successfully."})

@transaction.atomic
def confirm_booking(request, show_id):
    seat_numbers = request.GET.getlist("seats")
    seats = (
        Seat.objects
        .select_for_update()
        .filter(show_id=show_id, seat_number__in=seat_numbers)
    )

    for seat in seats:
        if seat.status != Seat.HELD or seat.is_hold_expired():
            return JsonResponse({"error": "Seat hold expired"}, status=400)
        
    for seat in seats:
        seat.status = Seat.BOOKED
        seat.held_untill = None
        seat.save()

    return JsonResponse({"message": "Booking confirmed"})

def show_status(request, show_id):
    return JsonResponse({
        "available" : Seat.objects.filter(show_id=show_id, status=Seat.AVAILABLE).count(),
        "held" : Seat.objects.filter(show_id=show_id, status=Seat.HELD).count(),
        "booked" : Seat.objects.filter(show_id=show_id, status=Seat.BOOKED).count(),
    })