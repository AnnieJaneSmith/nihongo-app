from django.conf.urls import url
from django.contrib import admin

from blog import views
app_name = 'blog'

urlpatterns = [
    # url(r'^$', views.blog_list.as_view(), name='list'),
    # url(r'^(?P<slug>[\w-]+)/$', views.blog_detail.as_view(), name='main_unit'),
    # url(r'^(?P<slug>[\w-]+)/unit/$', views.unit_detail.as_view(), name='unit'),
    url(r'^$', "blog.views.blog_list", name='list'),
    url(r'^profile/$', "blog.views.profile", name="profile"),
    url(r'^result/$', "blog.views.result", name="result"),
    # url(r'^lookup/$', "blog.views.lookup", name="lookup"),
    # url(r'^(?P<question_id>[0-9]+)/word/$', views.lookup, name='lookup'),
    url(r'^(?P<slug>[\w-]+)/$', "blog.views.blog_detail", name='main_unit'),
    url(r'^(?P<slug>[\w-]+)/detail/$', "blog.views.unit_detail", name='unit'),
    url(r'^(?P<slug>[\w-]+)/theme/$', "blog.views.theme_detail", name='theme'),
    url(r'^(?P<slug>[\w-]+)/lookup/$', "blog.views.lookup", name='lookup'),
    url(r'^(?P<slug>[\w-]+)/test/$', "blog.views.test", name='test'),
    url(r'^(?P<slug>[\w-]+)/help/$', "blog.views.theme_help", name='help'),
    url(r'^(?P<slug>[\w-]+)/helpu/$', "blog.views.unit_help", name='helpu'),
    url(r'^create/$', "blog.views.blog_create"),
    url(r'^(?P<slug>[\w-]+)/edit/$', "blog.views.blog_update", name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', "blog.views.blog_delete"),
    ]