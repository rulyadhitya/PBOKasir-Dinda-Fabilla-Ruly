# Generated by Django 3.2.8 on 2021-11-16 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_product_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='product_code',
        ),
    ]
