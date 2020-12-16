from django.db import models

# Create your models here.
class SmsMessages(models.Model):
    message_id = models.IntegerField(verbose_name='ИД сообщения')
    phone = models.CharField(
        max_length=15, verbose_name='Номер', null=True, blank=True)
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


