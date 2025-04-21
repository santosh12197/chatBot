from django.urls import path

from bot.views import ChatbotView, SupportChatView


urlpatterns = [
    path("chatbot/", ChatbotView.as_view(), name="chatbot"),
    path("support_chat/", SupportChatView.as_view(), name="support_chat"),

]
