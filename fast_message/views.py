from django.shortcuts import render
from django.http import HttpResponse

import fast_message.devino_package as devino_package
from fast_message.models import Message


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
    Message.objects.create(message_id=message_id, phone=dest, channel='sms')

    return render(request, 'send_sms.html', {'id': message_id}
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

    message_id = devino_response.text[2:21]
    Message.objects.create(message_id=message_id, phone=dest, channel='viber')

    return render(
        request, 'send_viber.html', {'id': message_id}
    )


def get_status(request):
    if request.method != 'POST':
        return render(request, 'get_status.html')

    session_id = request.POST['session_id']
    channel = request.POST['channel']

    devino_client = devino_package.DevinoClient()

    messages = Message.objects.filter(state=None, channel=channel)

    for message in messages:
        devino_response = devino_client.get_status(
            channel, session_id, message.message_id
        )

        state = devino_response.json()['State']
        message.state = state

        state_desc = devino_response.json()['StateDescription']
        message.state_desc = state_desc

        timestamp = devino_client.get_ts_from_response(
            devino_response, 'SubmittedDateUtc'
        )
        message.set_submit_dt_from_ts(timestamp)

        timestamp = devino_client.get_ts_from_response(
            devino_response, 'ReportedDateUtc'
        )
        message.set_report_dt_from_ts(timestamp)

        message.save()

    return render(request, 'get_status.html', {'got_statuses': True})

