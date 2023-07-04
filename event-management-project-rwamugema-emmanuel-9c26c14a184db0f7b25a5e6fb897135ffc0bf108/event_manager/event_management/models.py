from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_free = models.BooleanField(default=True)
    def __str__(self):
        return self.title 

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    photo = models.ImageField(upload_to='speakers', blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.name



class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    topic = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.topic

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed')
    )
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    payment_date = models.DateField()
    transaction_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.participant.name} - {self.event.title}"

