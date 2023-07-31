from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages


def escaperoom_page_view(request):
    return render(request, 'escaperoom.html')


def reservation_page_view(request):
    return render(request, 'reservation.html')


def booking(request):
    weekdays = validWeekday(31)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        room = request.POST.get('room')
        day = request.POST.get('day')
        if room == None:
            messages.success(request, "Please Select A Room!")
            return redirect('booking')

        request.session['day'] = day
        request.session['room'] = room

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = ["9 AM", "10:30 AM", "12:00 PM", "1:30 PM",
             "3:00 PM", "4:30 PM", "6:00 PM", "7:30 PM", "9:00 PM"]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    room = request.session.get('room')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if room != None:
            if day <= maxDate and day >= minDate:
                if Reservation.objects.filter(day=day, room=room).count() < 8:
                    if Reservation.objects.filter(day=day, time=time, room=room).count() < 1:
                        ReservationForm = Reservation.objects.get_or_create(
                            user=user,
                            room=room,
                            day=day,
                            time=time,
                        )
                        messages.success(request, "Booking Saved!")
                        return redirect('escaperoom.html')
                    else:
                        messages.success(
                            request, "The Selected Time Has Already Been Reserved!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(
                    request, "The Selected Date Isn't In The Correct Time Slot!")
        else:
            messages.success(request, "Please Select A Room!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday' or y == 'Saturday' or y == 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Reservation.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    x = []
    for k in times:
        if Reservation.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x
