# Generated by Django 2.2.1 on 2019-06-11 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0014_auto_20190610_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(default='', help_text='Your')),
                ('photo', models.ImageField(blank=True, default='default.jpg', help_text='Your Image', upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('likes', models.BooleanField(default=False, help_text='Likess')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
