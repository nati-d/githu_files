# Generated by Django 4.2.11 on 2024-04-09 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_teammembers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammembers',
            name='members',
        ),
        migrations.AddField(
            model_name='teammembers',
            name='members',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
            preserve_default=False,
        ),
    ]
