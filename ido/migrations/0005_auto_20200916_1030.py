# Generated by Django 3.1.1 on 2020-09-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0004_auto_20200915_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='mobile',
        ),
        migrations.AddField(
            model_name='survey',
            name='phone_num',
            field=models.CharField(default='', max_length=13),
        ),
    ]
