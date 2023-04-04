# Generated by Django 4.1.7 on 2023-04-04 00:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0002_alter_room_options_room_room_mates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_mates',
            field=models.ManyToManyField(blank=True, related_name='room_mates', to=settings.AUTH_USER_MODEL),
        ),
    ]
