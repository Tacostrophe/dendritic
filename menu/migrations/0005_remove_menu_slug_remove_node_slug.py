# Generated by Django 4.2 on 2023-04-11 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_node_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='node',
            name='slug',
        ),
    ]
