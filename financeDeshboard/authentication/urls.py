# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user,custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", custom_logout, name="logout")
    # path("logout/", LogoutView.as_view(), name="logout")
    # patterns('authentication.views',
    #          url(r'^view_profile/$', 'view_profile', name ='view_profile'),
    #          url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile')
    #          )
]
