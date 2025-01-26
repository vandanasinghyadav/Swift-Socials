# Generated by Django 5.0.2 on 2024-04-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_fname', models.CharField(max_length=30)),
                ('apply_lname', models.CharField(max_length=30)),
                ('apply_email', models.CharField(max_length=30)),
                ('apply_gender', models.CharField(max_length=30)),
                ('apply_pincode', models.CharField(max_length=30)),
                ('apply_phone', models.IntegerField()),
                ('apply_position', models.TextField()),
                ('apply_date', models.DateField()),
                ('apply_address', models.TextField()),
                ('apply_coverletter', models.TextField()),
                ('apply_resume', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
