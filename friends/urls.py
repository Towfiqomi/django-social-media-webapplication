from django.urls import path, re_path
from friends import views


urlpatterns = [
    path('friends/', views.timeline_friends, name='tfriends'),
    path('findfriends/', views.timeline_find_friends, name='ffriends'),
    path('friends/add/', views.friend_request_list, name='friendship_request_list'),

    re_path(r'^friends/(?P<operation>.+)/(?P<pk>\d+)/$', views.friends_relation, name='friends_matters'),
]
