from django.db import models

# Create your models here.

class Hours(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=128)

# """
# nazwa budynku >> data >> godzina wejścia >> godzina wyjścia >> notatka dodatkowa jeśli jest
# """