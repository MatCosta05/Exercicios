from django.db import models

# Create your models here.

from datetime import datetime as dt


class ProjFilm(models.Model):
    tittle = models.CharField(max_length=40)
    desc = models.TextField()
    time = models.TimeField()
    data = models.DateTimeField("Cadastrado em", default=dt.now())

    def __str__(self):
        return self.tittle
