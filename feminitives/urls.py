"""feminitives URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from dict import views as main
from words import views
from feminitives import views as logs


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main.index, name='index'),
    url(r'^index.html', main.index, name='index'),
    url(r'^q-a.html', main.qa, name='q-a'),
    url(r'^word_template/$', views.word_template),
    url(r'^words/', include('words.urls')),
    # url(r'^search/', include('haystack.urls')),

    url(r'^accounts/login/$', logs.login),
    url(r'^accounts/auth/$', logs.auth_view),
    url(r'^accounts/logout/$', logs.logout),
    url(r'^accounts/loggedin/$', logs.loggedin),
    url(r'^accounts/invalid/$', logs.invalid_login),
]

# if not settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#     urlpatterns += staticfiles_urlpatterns()
