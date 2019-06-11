from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Profile)
admin.site.register(models.Comment)
admin.site.register(models.Posts)
admin.site.register(models.PostComments)
admin.site.register(models.PostLikes)

