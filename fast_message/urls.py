from django.urls import path

from fast_message import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_session/', views.get_session, name='get_session'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('send_viber/', views.send_viber, name='send_viber')
]