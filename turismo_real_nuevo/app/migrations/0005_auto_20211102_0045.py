# Generated by Django 2.2.3 on 2021-11-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
