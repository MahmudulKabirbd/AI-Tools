# Generated by Django 4.1.7 on 2023-03-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
