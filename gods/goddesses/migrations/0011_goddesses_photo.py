# Generated by Django 4.2.1 on 2023-11-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goddesses', '0010_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goddesses',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos', verbose_name='Image'),
        ),
    ]