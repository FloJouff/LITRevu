# Generated by Django 5.0.4 on 2024-05-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
