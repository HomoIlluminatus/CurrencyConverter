# Generated by Django 5.0.4 on 2024-04-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyrate',
            name='currency_code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
