# Generated by Django 3.2.7 on 2021-09-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210928_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingame',
            name='player',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='posx',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='posy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='posz',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='rotx',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='roty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='rotz',
            field=models.IntegerField(default=0),
        ),
    ]
