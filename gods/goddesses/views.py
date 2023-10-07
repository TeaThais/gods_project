from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string

from goddesses.models import Goddesses

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add post', 'url_name': 'add_post'},
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Login', 'url_name': 'login'}
]

cats_db = [
    {'id': 1, 'name': 'Egypt'},
    {'id': 2, 'name': 'Mesopotamia'},
    {'id': 3, 'name': 'Greece'},
]


def index(request):
    posts = Goddesses.published.all()
    data = {
        'title': "Goddesses",
        'menu': menu,
        'posts': posts,
        'url': slugify("press here for the next page"),
        'cat_selected': 0,
    }
    return render(request, 'goddesses/index.html', context=data)


def about(request):
    data = {
        'title': "About",
        'text': "About this site",
        'menu': menu,
    }
    return render(request, 'goddesses/about.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Goddesses, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'goddesses/post.html', data)


def add_post(request):
    return HttpResponse('Add post')


def contacts(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def show_category(request, cat_id):
    posts = Goddesses.objects.all()
    data = {
        'title': "Myth country",
        'menu': menu,
        'url': slugify("press here for the next page"),
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'goddesses/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')