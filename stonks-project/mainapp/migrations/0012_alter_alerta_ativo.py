# Generated by Django 4.0.5 on 2022-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_alerta_email_ativo_alter_alerta_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='ativo',
            field=models.CharField(max_length=10),
        ),
    ]