# Generated by Django 4.1.3 on 2023-05-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.IntegerField(),
        ),
    ]
