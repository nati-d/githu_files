# Generated by Django 4.2.11 on 2024-05-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventslist',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='eventslist',
            name='time',
        ),
        migrations.AddField(
            model_name='eventslist',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventslist',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
