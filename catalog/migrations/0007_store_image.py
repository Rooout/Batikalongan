# Generated by Django 5.1.2 on 2024-10-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(default=1, upload_to='store/'),
            preserve_default=False,
        ),
    ]
