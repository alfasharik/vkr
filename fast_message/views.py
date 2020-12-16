from django.shortcuts import render
from django.http import HttpResponse

import fast_message.devino_package as devino_package
# Create your views here.

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

    return render(
        request, 'send_sms.html', {'devino_response': devino_response}
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