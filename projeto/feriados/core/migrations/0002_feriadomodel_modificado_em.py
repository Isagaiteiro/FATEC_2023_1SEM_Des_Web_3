# Generated by Django 4.1.7 on 2023-04-05 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feriadomodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em:'),
        ),
    ]
