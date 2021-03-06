# Generated by Django 2.2.5 on 2021-04-10 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('aadhar_number', models.BigIntegerField(max_length=16)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=6)),
                ('date_of_birth', models.DateField()),
                ('mediclaim_number', models.IntegerField(max_length=5)),
                ('phone_number', models.BigIntegerField(max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=25)),
                ('health_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
    ]
