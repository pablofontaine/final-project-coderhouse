# Generated by Django 4.1.3 on 2022-11-26 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_new_unique_together_remove_new_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='author',
        ),
    ]
