# Generated by Django 3.2.12 on 2022-06-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0062_auto_20220619_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_all_seanses',
            name='ident_key',
            field=models.CharField(default='gkKYloRzteFsEiu', max_length=20, verbose_name='Специальный код сеанса'),
        ),
        migrations.AlterField(
            model_name='data_all_seanses',
            name='summa',
            field=models.IntegerField(default=830, verbose_name='Цена билета'),
        ),
    ]
