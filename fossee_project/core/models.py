from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EventUpload(models.Model):
    EVENT_CHOICES = [
        ('Hackathon', 'Hackathon'),
        ('Workshop', 'Workshop'),
        ('Internship', 'Internship'),
        ('Orientation', 'Orientation'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    event_date = models.DateField()
    csv_file = models.FileField(upload_to='uploads/csvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event_type} ({self.event_date})"
