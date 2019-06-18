from django.db import models

# Create your models here.

class Vote(models.Model):
    colleges = [('CEDAT', 'College Of Engineering Design Art ANd Technology'),
                ('COBAMS', 'Economics')
                ]
    departments = []
    programs = []
    year = [('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]
    sexes = [('m', 'Male'), ('f', 'female'), ('u', 'undefined')]

    college = models.CharField(max_length=100, choices=colleges, help_text='From the dropdown menu select your college')
    department = models.CharField(max_length=100, help_text='Choose your department')
    program = models.CharField(max_length=50, help_text='What is your Program')
    year_of_study = models.CharField(max_length=4, choices=year, help_text='Select your your of study')
    full_name = models.CharField(max_length=100, help_text='Enter Your full official name')
    reg_no = models.CharField(max_length=20, primary_key=True, help_text='Enter your Registration number')
    student_no = models.CharField(max_length=20, default='', help_text='Your student number')
    date_of_birth = models.DateField(blank=True, null=True, help_text='Enter your birthday')
    email = models.EmailField(default='', help_text='The email will only be used for official purposes')
    photo = models.ImageField(blank=True, default='default.jpg', help_text='This will be your profile picture')
    sex = models.CharField(max_length=10, choices=sexes, help_text='Sex', default='')
    post = models.CharField(max_length=100, help_text='post of leadership')
    vote = models.BooleanField(help_text='student vote', default=False)
    nominated = models.BooleanField(help_text='Nominated Candidate', default=False)

    def __str__(self):
        return self.full_name