# Generated by Django 3.2.8 on 2021-11-16 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20211116_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Order Date (mm/dd/yyyy)*'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]