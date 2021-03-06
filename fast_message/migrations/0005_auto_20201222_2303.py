# Generated by Django 3.1.4 on 2020-12-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_message', '0004_auto_20201216_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField(verbose_name='ИД сообщения')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер')),
                ('channel', models.CharField(max_length=10, verbose_name='Канал')),
                ('state', models.IntegerField(blank=True, null=True, verbose_name='Статус')),
                ('state_desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='Описание статуса')),
                ('submit_dt', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
                ('report_dt', models.DateTimeField(blank=True, null=True, verbose_name='Дата доставки')),
            ],
        ),
        migrations.DeleteModel(
            name='SmsMessages',
        ),
    ]
