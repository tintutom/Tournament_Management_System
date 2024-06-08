from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

class Tournament(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirm', 'Confirm'),
    ]
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.TextField()
    contact_email = models.EmailField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    teams = models.ManyToManyField(Team)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tournament.name} - {self.date} - {self.location}"
