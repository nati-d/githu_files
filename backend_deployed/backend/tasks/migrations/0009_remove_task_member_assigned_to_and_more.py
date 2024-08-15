# Generated by Django 4.2.11 on 2024-04-29 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_alter_task_member_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_member',
            name='assigned_to',
        ),
        migrations.AlterField(
            model_name='task_member',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task_card'),
        ),
        migrations.AddField(
            model_name='task_member',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
