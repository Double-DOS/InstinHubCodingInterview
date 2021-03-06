# Generated by Django 3.2.5 on 2021-07-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_userimage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='activities',
            field=models.ManyToManyField(related_name='activties', to='dashboard.Activity'),
        ),
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
