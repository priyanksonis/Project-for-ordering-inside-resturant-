# Generated by Django 2.1.5 on 2019-03-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_auto_20190323_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchenorderbook',
            name='order_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]