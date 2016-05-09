# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about', TemplateView.as_view(template_name='about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}yeah he does
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('bizsprint.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^events', TemplateView.as_view(template_name='events.html'), name='events'),
    url(r'^blog', TemplateView.as_view(template_name='blog-single-small.html'), name='blog'),
    url(r'^faqs', TemplateView.as_view(template_name='faqs.html'), name='faqs'),
    url(r'^contact', TemplateView.as_view(template_name='forms.html'), name='contact'),
    url(r'^login', TemplateView.as_view(template_name='login-register.html'), name='login'),



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
