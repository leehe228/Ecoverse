# Generated by Django 3.2.7 on 2021-09-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_user_smartfarm_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='smartfarm_state',
            field=models.CharField(default='0-0-20210101000000-0-20210101000000', max_length=50),
        ),
    ]
