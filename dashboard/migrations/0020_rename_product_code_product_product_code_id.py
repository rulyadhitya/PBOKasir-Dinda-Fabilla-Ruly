# Generated by Django 3.2.8 on 2021-11-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20211117_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_code',
            new_name='product_code_id',
        ),
    ]
