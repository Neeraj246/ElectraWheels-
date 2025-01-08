# Generated by Django 5.1.4 on 2025-01-07 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evapp', '0018_remove_sparetable_station_sparetable_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparebookingtable',
            name='SLOT',
        ),
        migrations.AddField(
            model_name='sparebookingtable',
            name='SPARE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evapp.sparetable'),
        ),
        migrations.AlterField(
            model_name='sparebookingtable',
            name='USER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evapp.usertable'),
        ),
    ]
