from django.core.management.base import BaseCommand
from django.utils import timezone
from seats.models import SeatHold

class Command(BaseCommand):
    help = "Release expired seat holds"

    def handle(self, *args, **kwargs):
        expired = SeatHold.objects.filter(expires_at__lt=timezone.now())
        count = expired.count()

        for hold in expired:
            seat = hold.seat
            seat.status = "AVAILABLE"
            seat.save()
            hold.delete()

        self.stdout.write(f"Released {count} expired holds")