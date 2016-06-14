# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import, unicode_literals
import requests

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from bizsprint.users.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from bizsprint.users.forms import ContactForm, SignUpForm
from .models import Post
from .forms import PostForm

# response = requests.get(
#     "https://www.eventbriteapi.com/v3/users/me/owned_events/",
#     headers = {
#         "Authorization": "Bearer DYESB7ITMXX2FEYYQAH4",
#     },
#     verify = True,  # Verify SSL certificate
# )
# print response.json()['events'][0]['name']['text']

# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        # print request.POST['email'] #not recommended
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        # 	instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            # for key, value in form.cleaned_data.iteritems():
            #  print key, value
            #  #print form.cleaned_data.get(key)
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            form_full_name = form.cleaned_data.get("full_name")
            # print email, message, full_name
            subject = 'Site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'youotheremail@email.com']
            contact_message = "%s: %s via %s" % (
                form_full_name,
                form_message,
                form_email)
            some_html_message = "\n<h1>Hello from Bizsprint</h1>\n"
            send_mail(subject, contact_message, from_email, to_email, html_message=some_html_message, fail_silently=False)

        context = {
            "form": form,
            "title": title,
            "title_align_center": title_align_center,
        }
        return HttpResponseRedirect("/confirmation/")
    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "contact.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "bizblog.html", context)

def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Post Error")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance,
        "title": instance.title,
    }
    return render(request, "post_detail.html", context)

def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "title": instance.title,
        "form": form,
    }
    return render(request, "post_form.html", context)

def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted")
    return redirect("posts")


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
