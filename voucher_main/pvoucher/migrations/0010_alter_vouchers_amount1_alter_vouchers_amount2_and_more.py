# Generated by Django 4.1 on 2023-03-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvoucher', '0009_alter_vouchers_amount2_alter_vouchers_amount3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='amount1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='amount2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='amount3',
            field=models.IntegerField(blank=True),
        ),
    ]
