from django.contrib import admin

from fast_message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'message_id', 'phone', 'channel', 'state', 'state_desc',
        'submit_dt', 'report_dt'
    ]
    search_fields = [
        'message_id', 'phone', 'channel', 'state', 'state_desc',
        'submit_dt', 'report_dt'
    ]
    list_filter = [
        'message_id', 'phone', 'channel', 'state', 'state_desc',
        'submit_dt', 'report_dt'
    ]
    empty_value_display = '-пусто-'


admin.site.register(Message, MessageAdmin)