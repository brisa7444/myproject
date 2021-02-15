from django.urls import path
from . import views
app_name='firewall'

urlpatterns = [
    path('',views.index,name='index'),
    path('WAFLogin',views.WAFLogin,name='WAFLogin'),
    path('searchWaiting',views.searchWaiting,name='searchWaiting'),
    path('logShow',views.logShow,name='logShow'),
    path('blacklistShow',views.blacklistShow,name='blacklistShow'),
    path('whitelistShow',views.whitelistShow,name='whitelistShow'),
    path('ruleChange',views.ruleChange,name='ruleChange'),
]