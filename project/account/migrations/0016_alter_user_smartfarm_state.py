# Generated by Django 3.2.7 on 2021-09-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_user_badge_subinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='smartfarm_state',
            field=models.CharField(default='0-0-2021/01/01 00:00:00-0-2021/01/01 00:00:00', max_length=50),
        ),
    ]
