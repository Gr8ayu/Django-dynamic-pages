from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Posts


# Create your views here.

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Posts
    fields = ['creationDate', 'type', 'title', 'content', 'publish', ]


@method_decorator(login_required, name='dispatch')
class PostList(ListView):
    template_name = 'blogs/postlist.html'

    def get_queryset(self):
        return Posts.objects.filter(publish=True)


@method_decorator(login_required, name='dispatch')
class PostDetail(DetailView):
    model = Posts
    template_name = 'blogs/postdetail.html'
