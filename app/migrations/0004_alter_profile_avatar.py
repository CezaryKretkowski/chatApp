# Generated by Django 4.1.7 on 2023-03-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/Resource/default.jpg', upload_to='Resource/users'),
        ),
    ]