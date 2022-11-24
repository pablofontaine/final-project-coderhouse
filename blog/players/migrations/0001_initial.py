# Generated by Django 4.1.3 on 2022-11-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TennisPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=15)),
                ('retired', models.BooleanField(default=True)),
            ],
        ),
    ]
