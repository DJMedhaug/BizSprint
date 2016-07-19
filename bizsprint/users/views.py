# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bizsprint.users.models import User
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from bizsprint.users.forms import ContactForm, SignUpForm


# Create your views here.


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Tiny Spot contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]  # add more emails as a string if needed
        contact_message = "%s: %s via %s" % (
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)

        context = {
            "form": form,
            "title": title,
            "title_align_center": title_align_center,
        }
        return HttpResponseRedirect("/confirmation/")

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "contact.html", context)





class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
