# Generated by Django 4.1.7 on 2023-03-19 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_stasus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='stasus',
            new_name='status',
        ),
    ]
