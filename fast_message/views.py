from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

import fast_message.devino_package as devino_package
from fast_message.models import Message
from fast_message.forms import SendForm, SessionForm, StatusForm


def index(request):
    return render(request, 'index.html')


def get_session(request):
    form = SessionForm(request.POST or None)

    if request.method != 'POST' or not form.is_valid():
        return render(request, 'get_session.html', {'form': form})

    login = form.cleaned_data['login']
    password = form.cleaned_data['password']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.get_session(login, password)

    return render(
        request, 'get_session.html',
        {'devino_response': devino_response, 'form':form}
    )


def send_sms(request):
    form = SendForm(request.POST or None)

    if request.method != 'POST' or not form.is_valid():
        return render(request, 'send_sms.html', {'form': form})

    session_id = form.cleaned_data['session_id']
    source = form.cleaned_data['source']
    dest = form.cleaned_data['dest']
    data = form.cleaned_data['data']
    validity = form.cleaned_data['validity']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.send_sms(
        session_id, source, dest, data, validity
    )

    message_id = devino_response.text[2:20]
    Message.objects.create(message_id=message_id, phone=dest, channel='sms')

    return render(
        request, 'send_sms.html', {'id': message_id, 'form': form})

def send_viber(request):
    form = SendForm(request.POST or None)

    if request.method != 'POST' or not form.is_valid():
        return render(request, 'send_viber.html', {'form': form})

    session_id = form.cleaned_data['session_id']
    source = form.cleaned_data['source']
    dest = form.cleaned_data['dest']
    data = form.cleaned_data['data']
    validity = form.cleaned_data['validity']

    devino_client = devino_package.DevinoClient()
    devino_response = devino_client.send_viber(
        session_id, source, dest, data, validity
    )

    message_id = devino_response.text[2:21]
    Message.objects.create(message_id=message_id, phone=dest, channel='viber')

    return render(
        request, 'send_viber.html', {'id': message_id, 'form': form}
    )


def get_status(request):
    form = StatusForm(request.POST or None)

    if request.method != 'POST' or not form.is_valid():
        return render(request, 'get_status.html', {'form': form})

    session_id = form.cleaned_data['session_id']
    channel = form.cleaned_data['channel']

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

    return render(
        request, 'get_status.html', {'got_statuses': True, 'form':form}
    )


def detail(request):
    messages = Message.objects.all().order_by('-report_dt')

    paginator = Paginator(messages, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'detail.html', {'page': page, 'paginator': paginator})

