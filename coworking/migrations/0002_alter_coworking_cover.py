# Generated by Django 5.0.4 on 2024-04-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworking',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='coworkings/covers/%Y/%m/%d/'),
        ),
    ]
