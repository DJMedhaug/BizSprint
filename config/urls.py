# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from bizsprint.users import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', TemplateView.as_view(template_name='about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}yeah he does
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('bizsprint.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^events', TemplateView.as_view(template_name='events.html'), name='events'),
    url(r'^blog', TemplateView.as_view(template_name='bizblog.html'), name='blog'),
    url(r'^faqs', TemplateView.as_view(template_name='faqs.html'), name='faqs'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^confirmation', TemplateView.as_view(template_name='confirmation.html'), name='confirmation'),
    #url(r'^login', TemplateView.as_view(template_name='login-register.html'), name='login'),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/users/', include("signin.api.urls", namespace='users-api')),
    url(r'^api/comments/', include("comments.api.urls", namespace='comments-api')),
    url(r'^api/posts/', include("posts.api.urls", namespace='posts-api')),
    url(r'^register/', include("signin.urls", namespace='signin')),
    url(r'^signin/', include("signin.urls", namespace='signin')),
    url(r'^signout/', include("signin.urls", namespace='signin')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
