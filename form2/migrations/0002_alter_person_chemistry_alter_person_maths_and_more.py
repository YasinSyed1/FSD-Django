# Generated by Django 5.1.2 on 2024-11-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='chemistry',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='maths',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='physics',
            field=models.IntegerField(),
        ),
    ]
