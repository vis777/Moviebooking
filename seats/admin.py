from django.contrib import admin
from .models import Show, Seat


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "show_time", "total_seats")
    search_fields = ("movie_name",)
    list_filter = ("show_time",)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat_number", "show", "status", "held_until")
    list_filter = ("status", "show")
    search_fields = ("seat_number",)