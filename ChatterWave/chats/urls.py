from django.urls import path
from . import views

urlpatterns=[
    path('',views.messages_page,name='message_page'),
]