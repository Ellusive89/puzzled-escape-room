from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

ROOM_CHOICES = (
    ("Lost in Time", "Lost in Time"),
    ("Enchanted Forest", "Enchanted Forest"),
    ("Space Odyssey", "Space Odyssey"),
    ("The Haunted Manor", "The Haunted Manor"),
    ("Art Heist", "Art Heist"),
    ("Survival Island", "Survival Island"),
    ("Carnival of Curiosities", "Carnival of Curiosities"),
    ("Egyptian Tomb", "Egyptian Tomb"),
)

TIME_CHOICES = (
    ("9:00 AM", "9:00 AM"),
    ("10:30 AM", "10:30 AM"),
    ("12:00 PM", "12:00 PM"),
    ("1:30 PM", "1:30 PM"),
    ("3:00 PM", "3:00 PM"),
    ("4:30 PM", "4:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("9:00 PM", "9:00 PM"),
)

PLAYER_NUMBER_CHOICES = [(i, str(i)) for i in range(2, 9)]


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    room = models.CharField(
        max_length=50, choices=ROOM_CHOICES, default="Lost in Time")
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="9:00 AM")
    players = models.IntegerField(choices=PLAYER_NUMBER_CHOICES, default=2)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | room: {self.room} | day: {self.day} | time: {self.time} | players: {self.players}"


class Room_Description(models.Model):
    title = models.CharField(max_length=500)
    short_description = models.CharField(max_length=1000)
    long_description = models.TextField()
    image = CloudinaryField('image')
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.title
