from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'website.views.index'),
    url(r'^page/(\d+)/$', 'website.views.page'),
    url(r'^admin/', include(admin.site.urls)),
)
