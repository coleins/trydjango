# Generated by Django 5.2 on 2025-04-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(default='this is cool'),
        ),
    ]
