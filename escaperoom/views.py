from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
from .models import Room_Description


def escaperoom_page_view(request):
    # Render the escaperoom page with 'puzzled' as the active tab.
    return render(request, 'escaperoom.html', {'active_tab': 'puzzled'})


def contact(request):
    # Render the contact page with 'contact' as the active tab.
    return render(request, 'contact.html', {'active_tab': 'contact'})


def booking(request):
    # Generate and validate weekdays
    weekdays = validWeekday(31)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        room = request.POST.get('room')
        day = request.POST.get('day')

        # Ensure a room is selected before proceeding
        if room == None:
            messages.success(request, "Please Select A Room!")
            return redirect('booking')

        # Store room and day in the session for later retrieval
        request.session['day'] = day
        request.session['room'] = room

        return redirect('bookingSubmit')

    # Render the booking page with weekdays data and active tab
    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'active_tab': 'booking',
    })


def bookingSubmit(request):
    # Get the current user and set up time slots and date ranges
    user = request.user
    times = ["9 AM", "10:30 AM", "12:00 PM", "1:30 PM",
             "3:00 PM", "4:30 PM", "6:00 PM", "7:30 PM", "9:00 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    room = request.session.get('room')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        players = int(request.POST.get("players"))
        date = dayToWeekday(day)

        # Validate the room, date, and availability before creating a reservation
        if room != None:
            if day <= maxDate and day >= minDate:
                if Reservation.objects.filter(day=day, room=room).count() < 8:
                    if Reservation.objects.filter(day=day, time=time, room=room).count() < 1:
                        ReservationForm = Reservation.objects.get_or_create(
                            user=user,
                            room=room,
                            day=day,
                            time=time,
                            players=players
                        )
                        messages.success(request, "Your Booking Is Now Saved!")
                        return redirect('escaperoom.html')
                    else:
                        messages.success(
                            request, "The Selected Time Has Already Been Reserved!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(
                    request, "The Selected Date Does Not Match The Expected Time Frame!")
        else:
            messages.success(request, "Please Select A Room!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
        'player_number_choices': PLAYER_NUMBER_CHOICES
    })


def dayToWeekday(x):
    # Convert a date string to its corresponding weekday name.
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Return a list of valid weekdays (excluding Monday) up to the specified number of days from today.
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    # Filter out weekdays that have more than 8 reservations.
    validateWeekdays = []
    for j in x:
        if Reservation.objects.filter(day=j).count() < 8:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Return available times for a given day based on existing reservations.
    x = []
    for k in times:
        if Reservation.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def our_rooms(request):
    # Render the 'our_rooms' page with a list of all room descriptions.
    rooms = Room_Description.objects.all()
    context = {'rooms': rooms, 'active_tab': 'our_rooms'}
    return render(request, 'our_rooms.html', context)


def user_panel(request):
    # Render the 'our_rooms' page with a list of all room descriptions.
    user = request.user
    now = datetime.now()
    reservations = Reservation.objects.filter(
        user=user,
        day__gte=now.date(),
        time__gte=now.time()
    ).exclude(
        day=now.date(),
        time__lt=now.time()
    ).order_by('day', 'time')

    return render(request, 'user_panel.html', {
        'user': user,
        'reservations': reservations,
    })


def user_update(request, id):
    # Update the reservation details of a user, ensuring changes are made at least 24 hours in advance.
    reservation = Reservation.objects.get(pk=id)
    userdatepicked = reservation.day

    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    delta24 = (userdatepicked).strftime(
        '%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')

    weekdays = validWeekday(31)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        room = request.POST.get('room')
        day = request.POST.get('day')

        request.session['day'] = day
        request.session['room'] = room

        return redirect('user_updateSubmit', id=id)

    return render(request, 'user_update.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id,
    })


def user_updateSubmit(request, id):
    # Process user's request to edit their reservation, validating time slots and dates before updating the booking.
    user = request.user
    times = ["9 AM", "10:30 AM", "12:00 PM", "1:30 PM", "3:00 PM",
             "4:30 PM", "6:00 PM", "7:30 PM", "9:00 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=31)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    room = request.session.get('room')

    hour = checkTime(times, day)
    reservation = Reservation.objects.get(pk=id)
    userSelectedTime = reservation.time
    if request.method == 'POST':
        time = request.POST.get("time")
        players = int(request.POST.get("players"))
        date = dayToWeekday(day)

        if room != None:
            if day <= maxDate and day >= minDate:
                if date in ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                    if Reservation.objects.filter(day=day, room=room).count() < 8:
                        if Reservation.objects.filter(day=day, time=time, room=room).count() < 1 or userSelectedTime == time:
                            ReservationForm = Reservation.objects.filter(pk=id).update(
                                user=user,
                                room=room,
                                day=day,
                                time=time,
                                players=players
                            )
                        messages.success(
                            request, "Your Booking Has Been Edited!")
                        return redirect('escaperoom')
                    else:
                        messages.success(
                            request, "The Selected Time Has Already Been Reserved!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(
                    request, "The Selected Date Does Not Match The Expected Time Frame!")
        else:
            messages.success(request, "Please Select A Room!")
        return redirect('user_panel')

    return render(request, 'user_updateSubmit.html', {
        'times': hour,
        'player_number_choices': PLAYER_NUMBER_CHOICES,
        'id': id,
        'reservation': reservation,
    })


def checkEditTime(times, day, id):
    # Return available time slots for editing a reservation, including the user's current reservation time.
    x = []
    reservation = Reservation.objects.get(pk=id)
    time = reservation.time
    room = reservation.room
    for k in times:
        if Reservation.objects.filter(day=day, time=k, room=room).count() < 1 or time == k:
            x.append(k)
    return x


def user_delete(request, id):
    # Allow the user to delete their reservation if it's more than 48 hours before the booked time.
    reservation = get_object_or_404(Reservation, pk=id)
    user_date_picked = reservation.day
    today = datetime.today().date()
    delta_48 = today + timedelta(days=2)

    if user_date_picked >= delta_48:
        if request.method == 'POST':
            if 'confirm' in request.POST:
                reservation.delete()
                messages.success(
                    request, "Your Reservation Has Been Canceled Successfully!")
                return redirect('user_panel')
            else:
                return redirect('user_panel')

        return render(request, 'delete_reservation.html', {'reservation': reservation})
    else:
        messages.error(
            request, "Sorry, You Can Only Cancel A Reservation More Than 48 Hours Before Your Original Booking.")
        return redirect('user_panel')
