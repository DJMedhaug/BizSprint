from django.conf.urls import url
from django.contrib import admin

from .views import (
    login_view,
    register_view,
    logout_view

    )

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
]