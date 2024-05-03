# Generated by Django 5.0.4 on 2024-05-02 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.CharField(max_length=100)),
                ('train_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('availability_of_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('aadhar_no', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('security_ques', models.CharField(max_length=255)),
                ('security_ans', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TrainStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100)),
                ('station_no', models.IntegerField()),
                ('arrival_time', models.DateTimeField()),
                ('hault', models.IntegerField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.train')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('no_of_passengers', models.IntegerField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.train')),
                ('booked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.user')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('pnr_no', models.CharField(max_length=100)),
                ('seat_no', models.CharField(max_length=100)),
                ('reservation_status', models.CharField(max_length=100)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.user')),
            ],
        ),
    ]
