# Generated by Django 4.2.7 on 2023-11-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_study_dream', '0002_recorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recorder',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='recorder',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
