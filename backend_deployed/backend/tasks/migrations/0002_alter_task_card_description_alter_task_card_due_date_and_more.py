# Generated by Django 4.2.11 on 2024-03-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_card',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task_card',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task_card',
            name='status',
            field=models.CharField(choices=[('1', 'On progress'), ('2', 'Not yet started'), ('3', 'Interupted'), ('3', 'Completed')], default='1', max_length=1),
        ),
    ]
