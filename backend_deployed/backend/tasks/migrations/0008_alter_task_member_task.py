# Generated by Django 4.2.11 on 2024-04-28 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_task_member_assigned_to_taskassignment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_member',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task_card'),
        ),
    ]
