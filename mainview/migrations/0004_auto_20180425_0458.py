# Generated by Django 2.0.4 on 2018-04-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainview', '0003_auto_20180425_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
