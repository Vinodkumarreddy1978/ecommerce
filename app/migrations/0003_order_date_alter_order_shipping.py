# Generated by Django 4.2.4 on 2023-08-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_order_payment_id_alter_order_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.IntegerField(default=50),
        ),
    ]