from django.conf.urls import url, include

from .views import MainpageView, HistoryListView, FaqListView,ChatListView


urlpatterns = [
	url(r'^chat/', ChatListView.as_view(), name='chat'),
    url(r'^history/', HistoryListView.as_view(), name='history'),
    url(r'^faq/', FaqListView.as_view(), name='faq'),
    url(r'^', MainpageView.as_view(), name='mainpage')
]
