from django.urls import path
from .views import hold_seats, confirm_booking, show_status

urlpatterns = [
    path("hold/<int:show_id>/", hold_seats),
    path("book/<int:show_id>/", confirm_booking),
    path("status/<int:show_id>/", show_status),
]