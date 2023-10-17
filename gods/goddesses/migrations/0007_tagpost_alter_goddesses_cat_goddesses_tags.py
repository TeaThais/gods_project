# Generated by Django 4.2.1 on 2023-10-12 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goddesses', '0006_alter_goddesses_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='goddesses',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deities', to='goddesses.category'),
        ),
        migrations.AddField(
            model_name='goddesses',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='post_tags', to='goddesses.tagpost'),
        ),
    ]
