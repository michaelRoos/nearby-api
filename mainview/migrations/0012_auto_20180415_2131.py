# Generated by Django 2.0.4 on 2018-04-15 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainview', '0011_auto_20180415_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'events'},
        ),
        migrations.AlterModelOptions(
            name='event_categories',
            options={'verbose_name_plural': 'event_categories'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'images'},
        ),
        migrations.AlterModelOptions(
            name='times',
            options={'verbose_name_plural': 'times'},
        ),
        migrations.AlterModelOptions(
            name='upvotes',
            options={'verbose_name_plural': 'upvotes'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='zip_location',
            options={'verbose_name_plural': 'zip_locations'},
        ),
    ]