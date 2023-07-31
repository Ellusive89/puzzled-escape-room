# Generated by Django 4.2.3 on 2023-07-31 15:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(choices=[('Lost in Time', 'Lost in Time'), ('Enchanted Forest', 'Enchanted Forest'), ('Space Odyssey', 'Space Odyssey'), ('The Haunted Manor', 'The Haunted Manor'), ('Art Heist', 'Art Heist'), ('Survival Island', 'Survival Island'), ('Carnival of Curiosities', 'Carnival of Curiosities'), ('Egyptian Tomb', 'Egyptian Tomb')], default='Lost in Time', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('9:00 AM', '9:00 AM'), ('10:30 AM', '10:30 AM'), ('12:00 PM', '12:00 PM'), ('1:30 PM', '1:30 PM'), ('3:00 PM', '3:00 PM'), ('4:30 PM', '4:30 PM'), ('6:00 PM', '6:00 PM'), ('7:30 PM', '7:30 PM'), ('9:00 PM', '9:00 PM')], default='9:00 AM', max_length=10)),
                ('players', models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=2)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
