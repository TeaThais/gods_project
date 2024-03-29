# Generated by Django 4.2.1 on 2023-10-17 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goddesses', '0007_tagpost_alter_goddesses_cat_goddesses_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='goddesses',
            name='consort',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consort', to='goddesses.consort'),
        ),
    ]
