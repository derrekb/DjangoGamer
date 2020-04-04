from django.conf.urls import url
from django.contrib import admin
from search.views import (searchposts)

app_name = 'search'

urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),

]