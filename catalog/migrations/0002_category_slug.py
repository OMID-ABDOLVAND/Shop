# Generated by Django 5.0 on 2023-12-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=models.CharField(db_index=True, max_length=255)),
        ),
    ]
