from django.db import models
from track.models import Track


class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, db_column='track_id')
