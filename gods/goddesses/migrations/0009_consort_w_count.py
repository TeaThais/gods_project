# Generated by Django 4.2.1 on 2023-10-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goddesses', '0008_consort_goddesses_consort'),
    ]

    operations = [
        migrations.AddField(
            model_name='consort',
            name='w_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
