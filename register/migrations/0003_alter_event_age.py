# Generated by Django 4.2.2 on 2023-07-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_rename_eid_event_aid_remove_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]