# Generated by Django 4.1 on 2022-09-01 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='produt',
            new_name='prodt',
        ),
    ]
