# Generated by Django 3.2.12 on 2022-05-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0004_auto_20220529_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isGreen',
            field=models.BooleanField(default=0, verbose_name='Показатель если пользоветель по лицу то true'),
        ),
        migrations.AlterField(
            model_name='data_all_seanses',
            name='ident_key',
            field=models.CharField(default='FkpRqCIsudGYJnz', max_length=20, verbose_name='Специальный код сеанса'),
        ),
        migrations.AlterField(
            model_name='data_all_seanses',
            name='summa',
            field=models.IntegerField(default=1035, verbose_name='Цена билета'),
        ),
    ]
