from django import forms


class SendForm(forms.Form):
    session_id = forms.CharField(label='ИД Сессии:', max_length=40)
    source = forms.CharField(label='Имя отправителя:', max_length=15)
    dest = forms.CharField(label='Номер получателя:', max_length=15)
    data = forms.CharField(label='Текст:', widget=forms.Textarea)
    validity = forms.DecimalField(label='Время жизни:')


class SessionForm(forms.Form):
    login = forms.CharField(label='Логин:')
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput)


class StatusForm(forms.Form):
    session_id = forms.CharField(label='ИД Сессии:', max_length=40)

    CHOICES = [
        ('viber', 'viber'),
        ('sms', 'sms'),
    ]
    channel = forms.ChoiceField(
        label='Получить статусы', choices=CHOICES, widget=forms.RadioSelect
    )
