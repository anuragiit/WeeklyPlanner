# Generated by Django 2.0 on 2018-04-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_planner', '0002_auto_20180420_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='verified',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='TODO', max_length=200),
        ),
    ]
