# Generated by Django 5.1.4 on 2025-01-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evapp', '0006_remove_usertable_latitude_remove_usertable_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complainttable',
            name='Category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='complainttable',
            name='Description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='complainttable',
            name='Date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
