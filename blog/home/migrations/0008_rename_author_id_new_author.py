# Generated by Django 4.1.3 on 2022-11-27 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_new_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='author_id',
            new_name='author',
        ),
    ]