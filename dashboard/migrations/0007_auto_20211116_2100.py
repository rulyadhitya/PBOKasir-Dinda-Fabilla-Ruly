# Generated by Django 3.2.8 on 2021-11-16 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20211116_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
