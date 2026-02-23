from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["client", "table", "date", "start_time", "end_time", "guests_count",]