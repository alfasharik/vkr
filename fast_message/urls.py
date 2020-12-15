from django.urls import path

from fast_message import views


urlpatterns = [
    path('', views.index, name='index'),
    path('session/', views.session, name='session')
]