from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.FarmacoIndex.as_view(), name='index'),
)
