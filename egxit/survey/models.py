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

    position = models.CharField(max_length=3, choices=POSITION_CHOICES, blank=False)
    influences = models.ManyToManyField(Influences)
    additional_description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.position}"


class OtherPosition(models.Model):
    other_position = models.CharField(max_length=30, blank=False)


class WorkLifeMetrics(models.Model):
    RATING_CHOICES = {
        1: 'Strongly Disagree',
        2: 'Disagree',
        3: 'Neither Agree nor Disagree',
        4: 'Agree',
        5: 'Strongly Agree'    
    }
    
    attribute1 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute2 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute3 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute4 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute5 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute6 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute7 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute8 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute9 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute10 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute11 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute12 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute13 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute14 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute15 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute16 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute17 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute18 = models.IntegerField(choices=RATING_CHOICES, blank = False)
    attribute19 = models.IntegerField(choices=RATING_CHOICES, blank = False)


class OverallWorkExperience(models.Model):
    additional_workexp_description = models.CharField(max_length=500, blank=True)
    additional_leaving_description = models.CharField(max_length=500, blank=True)
    in_person_interview = models.BooleanField(blank = False)


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    phone = models.CharField(max_length=10, blank=False)    