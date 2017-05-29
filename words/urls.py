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
from django.views.generic import RedirectView
from words import views
from dict import views as main


urlpatterns = [
    url(r'^$', main.index, name='index'),
    url(r'^index.html', main.index, name='index'),
    url(r'^q-a.html', main.qa, name='q-a'),
    url(r'^all/$', views.words),
    url(r'^get/(?P<word_id>\d+)/$', views.word), #word id
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language), #language passed as a var
    url(r'^create/$', views.create),
    url(r'^search/$', views.search_words),
    # url(r'^search/', include('haystack.urls')),
]
