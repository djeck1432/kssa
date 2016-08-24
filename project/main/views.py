from django.shortcuts import render
from django.views.generic import ListView

from .models import Article, History, Faq


class MainpageView(ListView):
    model = Article
    template_name = 'index.html'
    paginate_by = 10
    allow_empty = True


class HistoryListView(ListView):
    model = History
    template_name = 'history.html'
    paginate_by = 10
    allow_empty = True


class FaqListView(ListView):
    model = Faq
    template_name = 'faq.html'
    allow_empty = True


class ChatListView(ListView):
    template_name = 'chat.html'
    paginate_by = 10
    allow_empty = True
