# Generated by Django 5.1.4 on 2025-01-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evapp', '0024_review_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slottable',
            name='Amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]