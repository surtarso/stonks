# Generated by Django 4.0.5 on 2022-06-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_stockdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='aceito',
            field=models.BooleanField(default=True),
        ),
    ]