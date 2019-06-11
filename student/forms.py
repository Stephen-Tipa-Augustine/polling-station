from django import forms
from . import models

import datetime
class StudentDetails(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = "__all__"
        labels = {
            'college':'Your College', 'department':'Your department', 'program':'Your Program',
            'year_of_study':'Year of study', 'full_name':'Full Name', 'reg_no':'Registration number',
            'date_of_birth':'Date of Birth', 'email':'Your Email', 'photo':'Select a photo',
            'mobile':'Mobile number', 'phone':'Phone number'
        }
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=[i for i in range(datetime.date.today().year, 1900, -1)])
        }
        help_texts={
            'photo': 'As your profile picture'
        }

class Post( forms.ModelForm ):
    class Meta:
        model = models.Posts
        fields = ['post', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
class PostComment(forms.ModelForm):
    class Meta:
        model = models.PostComments
        fields = ['comment']

class Like(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ['likes']
class Comment(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ['comments']



