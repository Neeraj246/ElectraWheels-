# Generated by Django 5.1.4 on 2025-01-07 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evapp', '0023_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='STATION',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evapp.stationtable'),
        ),
    ]