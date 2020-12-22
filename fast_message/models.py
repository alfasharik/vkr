from datetime import datetime

from django.db import models


class Message(models.Model):
    message_id = models.IntegerField(verbose_name='ИД сообщения')
    phone = models.CharField(
        max_length=15, verbose_name='Номер', null=True, blank=True)
    channel = models.CharField(verbose_name='Канал', max_length=10)
    state = models.IntegerField(verbose_name='Статус', null=True, blank=True)
    state_desc = models.CharField(
        max_length=50, verbose_name='Описание статуса', null=True, blank=True
    )
    submit_dt = models.DateTimeField(
        verbose_name='Дата отправки', null=True, blank=True
    )
    report_dt = models.DateTimeField(
        verbose_name='Дата доставки', null=True, blank=True
    )


    def set_submit_dt_from_ts(self, timestamp):
        submit_dt = datetime.fromtimestamp(timestamp)
        self.submit_dt = submit_dt

    def set_report_dt_from_ts(self, timestamp):
        report_dt = datetime.fromtimestamp(timestamp)
        self.report_dt = report_dt
