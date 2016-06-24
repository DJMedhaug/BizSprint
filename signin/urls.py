from django.conf.urls import url
from django.contrib import admin

from .views import (
    login_view,
    register_view,
    logout_view,

    )

urlpatterns = [
    url(r'^signin/', login_view, name='signin'),
    url(r'^signout/', logout_view, name='signout'),
    url(r'^register/', register_view, name='register'),
]