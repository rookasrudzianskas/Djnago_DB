# Generated by Django 3.2 on 2021-04-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(),
        ),
    ]
