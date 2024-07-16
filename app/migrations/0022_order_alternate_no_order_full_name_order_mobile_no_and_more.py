# Generated by Django 4.2.5 on 2023-09-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_order_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='alternate_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pin_code',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
    ]