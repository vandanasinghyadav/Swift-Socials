# Generated by Django 5.0.2 on 2024-04-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myteam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
