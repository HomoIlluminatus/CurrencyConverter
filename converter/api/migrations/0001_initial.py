# Generated by Django 5.0.4 on 2024-04-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=3)),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=10)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['currency_code'],
            },
        ),
    ]
