# Generated by Django 4.2.5 on 2023-09-15 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_order_address_alter_order_alternate_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
    ]