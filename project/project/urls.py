from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import RegisterFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login,
        {'template_name': 'enter.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^', include('main.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
