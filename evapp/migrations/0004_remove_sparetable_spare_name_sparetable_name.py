# Generated by Django 5.1.3 on 2024-12-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evapp', '0003_logintable_remove_userprofile_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparetable',
            name='Spare_name',
        ),
        migrations.AddField(
            model_name='sparetable',
            name='Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]