# Generated by Django 4.2.11 on 2024-03-29 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('1', 'On progress'), ('2', 'Not yet started'), ('3', 'Interupted'), ('3', 'Completed')], default='On progress', max_length=1)),
                ('due_date_reminder', models.CharField(choices=[('1', 'remind 1 days left'), ('2', 'remind 2 days left'), ('3', 'remind 3 days left')], default='O', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.activity_list')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
    ]
