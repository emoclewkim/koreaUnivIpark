# Generated by Django 3.1.6 on 2021-02-19 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0002_auto_20210216_2329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pastUser',
            new_name='historicalRecord',
        ),
        migrations.RenameModel(
            old_name='Survey',
            new_name='liveData',
        ),
        migrations.RenameModel(
            old_name='excelDB',
            new_name='memberData',
        ),
    ]
