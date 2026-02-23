from django.shortcuts import render, get_object_or_404
from .models import Client, Table, Booking

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


def home(request):
    return render(request, "home.html")


# Список активних столиків
def tables_list(request):
    tables = Table.objects.filter(is_active=True)

    return render(
        request,
        "tables_list.html",
        {"tables": tables}
    )


# Інформація про один столик
def table_detail(request, table_id):
    table = get_object_or_404(Table, id=table_id)

    return render(
        request,
        "table_detail.html",
        {"table": table}
    )


# Список клієнтів
def clients_list(request):
    clients = Client.objects.all()

    return render(
        request,
        "clients_list.html",
        {"clients": clients}
    )


# Інформація про одного клієнта
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    # усі бронювання цього клієнта
    bookings = Booking.objects.filter(client=client)

    return render(
        request,
        "client_detail.html",
        {
            "client": client,
            "bookings": bookings
        }
    )


# Бронювання на конкретну дату
def bookings_by_date(request):
    date = request.GET.get("date")
    bookings = None

    if date:
        bookings = Booking.objects.filter(date=date)

    return render(
        request,
        "bookings_by_date.html",
        {
            "bookings": bookings,
            "date": date
        }
    )


# Усі бронювання конкретного столика
def table_bookings(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    bookings = Booking.objects.filter(table=table)

    return render(
        request,
        "table_bookings.html",
        {
            "table": table,
            "bookings": bookings
        }
    )

@login_required(login_url='/accounts/login/')
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # прив’язуємо до користувача
            booking.save()
            return redirect("/table-booking/bookings/")  # куди після створення
    else:
        form = BookingForm()

    return render(request, "create_booking.html", {"form": form})