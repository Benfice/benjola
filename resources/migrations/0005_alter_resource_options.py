# Generated by Django 4.0.5 on 2023-01-21 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_alter_resource_teaser_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'permissions': [('special_status', 'Can see all resources')]},
        ),
    ]