# Generated by Django 3.2.12 on 2022-04-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_project_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.BooleanField(default=True),
        ),
    ]
