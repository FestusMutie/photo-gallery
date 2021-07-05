from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.photo,name = 'welcome'),
]