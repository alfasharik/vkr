from datetime import datetime
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse

import fast_message.devino_package as devino_package
from fast_message.models import SmsMessages


def index(request):
    return render(request, 'index.html')


def get_session(request):
    if request.method != 'POST':
        return render(request, 'session.html')

    login = request.POST['login']
    password = request.POST['password']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.get_session(login, password)

    return render(
        request, 'session.html',{'devino_response': devino_response}
    )


def send_sms(request):
    if request.method != 'POST':
        return render(request, 'send_sms.html')

    session_id = request.POST['session_id']
    source = request.POST['source']
    dest = request.POST['dest']
    data = request.POST['data']
    validity = request.POST['validity']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.send_sms(
        session_id, source, dest, data, validity
    )
    message_id = devino_response.text[2:20]
    SmsMessages.objects.create(message_id=message_id)

    return render(
        request, 'send_sms.html', {'id': message_id}
    )

def send_viber(request):
    if request.method != 'POST':
        return render(request, 'send_viber.html')

    session_id = request.POST['session_id']
    source = request.POST['source']
    dest = request.POST['dest']
    data = request.POST['data']
    validity = request.POST['validity']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.send_viber(
        session_id, source, dest, data, validity
    )

    return render(
        request, 'send_viber.html', {'devino_response': devino_response}
    )


def get_sms_status(request):
    devino_client = devino_package.DevinoClient()

    messages = SmsMessages.objects.filter(state=None)

    for message in messages:
        devino_response = devino_client.get_sms_status(
            '6425D63FD6164166B8E4B4980DE15983D661',
            message.message_id
        )

        timestamp = devino_response.json()['SubmittedDateUtc'][6:16]
        submit_dt = datetime.fromtimestamp(int(timestamp))

        message.submit_dt = submit_dt
        message.save()

    return render(request, 'detail.html', {'messages': messages})
# devino_response.json()['CreationDateUtc'][6:16]
# {"State":0,"CreationDateUtc":"\/Date(1608151480000)\/","SubmittedDateUtc":"\/Date(1608151480000)