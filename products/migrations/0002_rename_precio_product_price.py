# Generated by Django 5.2 on 2025-04-07 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
    ]
