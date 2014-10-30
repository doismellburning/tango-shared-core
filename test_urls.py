from django.conf.urls import url, patterns
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', lambda _: HttpResponse("Lorem Ipsum"), name='home'),
)
