# Generated by Django 3.2.7 on 2021-09-27 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20210928_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='energy_item_unlck',
            new_name='energy_item_unlock',
        ),
    ]
