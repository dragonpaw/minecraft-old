from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('dpminecraft.apps.minecraft.views',
    url(r'^items/$', 'item_index'),
    url(r'^item/([-\w]+)/$', 'item_detail'),
)
