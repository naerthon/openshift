from django.conf.urls import url
from .views			  import index, videos, concerts,all_concerts, about, news, detail_concerts

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^videos/$', videos, name='videos'),
    url(r'^concerts/$', concerts, name='concerts'),
    url(r'^all-concerts/$', all_concerts, name='all-concerts'),
    url(r'^concerts/(?P<pk>[0-9]+)/$', detail_concerts, name='detail-concerts'),
    url(r'^about/$', about, name='about'),
    url(r'^news/$', news, name='news'),
]

