# Generated by Django 3.1.7 on 2021-03-31 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30)),
                ('sbranch', models.CharField(max_length=30)),
                ('smarks', models.IntegerField(max_length=4)),
                ('sperc', models.FloatField(max_length=5)),
                ('srank', models.CharField(max_length=20)),
            ],
        ),
    ]
