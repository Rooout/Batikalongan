# Generated by Django 5.1.2 on 2024-10-23 18:01

import gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryentry',
            name='foto',
            field=models.ImageField(upload_to=gallery.models.rename_foto),
        ),
    ]
