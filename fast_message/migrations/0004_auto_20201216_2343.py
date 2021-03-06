# Generated by Django 3.1.4 on 2020-12-16 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_message', '0003_auto_20201216_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsmessages',
            name='report_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата доставки'),
        ),
        migrations.AlterField(
            model_name='smsmessages',
            name='state',
            field=models.IntegerField(blank=True, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='smsmessages',
            name='state_desc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Описание статуса'),
        ),
        migrations.AlterField(
            model_name='smsmessages',
            name='submit_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки'),
        ),
    ]
