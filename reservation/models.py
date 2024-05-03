from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    aadhar_no = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    security_ques = models.CharField(max_length=255)
    security_ans = models.CharField(max_length=255)

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    pnr_no = models.CharField(max_length=100)
    seat_no = models.CharField(max_length=100)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_status = models.CharField(max_length=100)

class Train(models.Model):
    train_no = models.CharField(max_length=100)
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    availability_of_seats = models.IntegerField()

class TrainStation(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=100)
    station_no = models.IntegerField()
    arrival_time = models.DateTimeField()
    hault = models.IntegerField()

class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    booked_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    no_of_passengers = models.IntegerField()
