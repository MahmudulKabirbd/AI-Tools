# Generated by Django 4.1.7 on 2023-03-19 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoty',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'All Posts'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
