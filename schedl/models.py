from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    details = models.CharField(max_length=200, null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email_id = models.EmailField()

    class Meta:
        unique_together = ('event', 'email_id')
