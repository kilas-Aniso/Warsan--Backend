# Generated by Django 3.2.6 on 2023-10-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20230930_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(choices=[('Banadir', 'Banadir'), ('Bari', 'Bari'), ('Bay', 'Bay'), ('Galguduud', 'Galguduud'), ('Gedo', 'Gedo'), ('Hiran', 'Hiran'), ('Jubbada_Dhexe', 'Jubbada Dhexe'), ('Jubbada_Hoose', 'Jubbada Hoose'), ('Mudug', 'Mudug'), ('Nugaal', 'Nugaal'), ('Sanaag', 'Sanaag'), ('Shabeellaha_Dhexe', 'Shabeellaha Dhexe'), ('Shabeellaha_Hoose', 'Shabeellaha Hoose'), ('Sool', 'Sool'), ('Togdheer', 'Togdheer'), ('Woqooyi_Galbeed', 'Woqooyi Galbeed'), ('Awdal', 'Awdal'), ('Bakool', 'Bakool'), ('Lower_Juba', 'Lower Juba')], default='Banadir', max_length=32, unique=True),
        ),
        migrations.AlterModelTable(
            name='location',
            table='Location',
        ),
    ]