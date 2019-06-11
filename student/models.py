from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Login(models.Model):
    reg_no = models.CharField(max_length=20)
    student_no = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.student_no
class Profile(models.Model):
    colleges = [('CEDAT', 'College Of Engineering Design Art ANd Technology'),
                ('COBAMS', 'Economics')
                ]
    departments = []
    programs = []
    year = [('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')]

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
    phone = models.CharField(max_length=10, default="")
    mobile = models.CharField(max_length=10, default="")
    def __str__(self):
        return self.full_name

class Comment(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    comment = models.TextField()
    photo = models.ImageField(help_text='An Image', blank=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment[:100]+'...'

class Posts(models.Model):
    photo = models.ImageField(blank=True, default='default.jpg', help_text='Your Image')
    post = models.TextField(help_text='Your post')
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(help_text='Likes', default=0)
    comments = models.IntegerField(help_text='comments', default=0)
    def __str__(self):
        return self.post[:100]+'...'

class PostComments(models.Model):
    post = models.TextField(help_text='Your', default='')
    photo = models.ImageField(blank=True, default='default.jpg', help_text='Your Image')
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(help_text='comments', default='')
    def __str__(self):
        return self.comment[:100]+'...'

class PostLikes(models.Model):
    post = models.TextField(help_text='Your', default='')
    photo = models.ImageField(blank=True, default='default.jpg', help_text='Your Image')
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.BooleanField(help_text='Likess', default=False)

    def __str__(self):
        return self.post[:100] + '...'
