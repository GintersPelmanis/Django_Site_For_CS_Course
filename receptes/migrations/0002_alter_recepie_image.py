# Generated by Django 4.1.5 on 2023-01-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='receptes/static/images'),
        ),
    ]
