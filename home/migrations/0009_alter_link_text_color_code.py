# Generated by Django 3.2.12 on 2022-04-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220427_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='text_color_code',
            field=models.CharField(default='#ffffff', max_length=50),
        ),
    ]