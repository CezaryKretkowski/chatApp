# Generated by Django 4.1.7 on 2023-04-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_frainds_friends_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='app.profile'),
        ),
        migrations.DeleteModel(
            name='Frainds',
        ),
    ]
