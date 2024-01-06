from django.db import models

class Influences(models.Model):
    INFLUENCES_CHOICES = {
        'A': 'Choice A',
        'B': 'Choice B',
        'C': 'Choice C',
        'D': 'Choice D',
        'E': 'Choice E',
        'F': 'Choice F',
        'G': 'Choice G',
        'H': 'Choice H',
        'I': 'Choice I',
        'J': 'Choice J'
    }
    name = models.CharField(max_length=1, choices=INFLUENCES_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Reasons(models.Model):

    POSITION_CHOICES = {
        'FTE':'Full Time Exemept Employee',
        'FTH':'Full Time Hourly Employee',
        'PTH':'Part Time Hourly Employee',
        'OT':'OTHER'
    }

    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    influences = models.ManyToManyField(Influences)
    additional_description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.position}"