# Generated by Django 3.2.3 on 2021-06-23 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='last_edit',
            new_name='lastedit',
        ),
    ]
