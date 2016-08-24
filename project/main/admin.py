from django.contrib import admin

from .models import Article, History, Faq


admin.site.register(Article)
admin.site.register(History)
admin.site.register(Faq)
