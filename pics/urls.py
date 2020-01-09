from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns= [
    url('^$', views.welcome, name = 'welcome'),
    url(r'^profile/(\d+)', views.profile, name = 'profile'),
    url(r'^profile/edit/profile', views.update_profile, name = 'update_profile'),
    url(r'^profile/create/post', views.create_post, name = 'create_posts'),
    url(r'^get_profile/(\d+)', views.get_profile, name='get_profile')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)