# Generated by Django 3.2.7 on 2021-09-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chat_regtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='regtime',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
