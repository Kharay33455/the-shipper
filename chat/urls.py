from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chats, name='chat'),
    path('chat/support-ticket<str:c_id>', views.chat, name = 'single_chat'),
    path('chat/create-new-chat', views.create_new_ticket, name='new_chat'),
]