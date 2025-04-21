from django.shortcuts import render
from django.views import View



class ChatbotView(View):

    def get(self, request):

        template_name = "chatbot.html"

        return render(request, template_name)


class SupportChatView(View):

    def get(self, request):

        template_name = "support_chat.html"

        return render(request, template_name)