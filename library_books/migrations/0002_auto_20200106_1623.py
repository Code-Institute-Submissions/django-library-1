# Generated by Django 3.0.2 on 2020-01-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='checkedOut',
            field=models.BooleanField(default=False),
        ),
    ]
