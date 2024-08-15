# Generated by Django 4.2.11 on 2024-06-02 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_member_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcard_attachment',
            name='path',
            field=models.FileField(blank=True, null=True, upload_to='project_files'),
        ),
        migrations.AlterField(
            model_name='taskcard_attachment',
            name='task_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task_card'),
        ),
    ]