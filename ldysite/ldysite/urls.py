"""ldysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^png','addr_book.views.png'),
    url(r'^$', 'addr_book.views.homepage'),
    url(r'^search1/$', 'addr_book.views.search1'),
    url(r'^search2/$', 'addr_book.views.search2'),
    url(r'^show/$', 'addr_book.views.show'),
    url(r'^show2/$', 'addr_book.views.show2'),
    url(r'^add/$', 'addr_book.views.add'),
    url(r'^add2/$', 'addr_book.views.add2'),
    url(r'^delete/$', 'addr_book.views.delete'),
    url(r'^update/$', 'addr_book.views.update'),
    url(r'^admin/', include(admin.site.urls)),
]
