# Generated by Django 5.0 on 2024-02-05 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='quantity',
        ),
        migrations.AddField(
            model_name='basket',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('commentary', models.TextField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.basket')),
            ],
        ),
    ]