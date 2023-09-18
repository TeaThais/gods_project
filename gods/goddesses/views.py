from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add post', 'url_name': 'add_post'},
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Login', 'url_name': 'login'}
]


data_db = [
    {'id': 1, 'name': 'Isis', 'content': 'Egyptian goddess', 'is_published': True},
    {'id': 2, 'name': 'Aphrodite', 'content': 'Greek goddess', 'is_published': False},
    {'id': 3, 'name': 'Hathor', 'content': 'Egyptian goddess', 'is_published': True},
    {'id': 4, 'name': 'Astarte', 'content': 'Sumerian goddess', 'is_published': True},
]


def index(request):
    # text = render_to_string('goddesses/index.html')
    # return HttpResponse(text)
    data = {
        'title': "the very first page",
        'menu': menu,
        'url': slugify("press here for the next page"),
        'posts': data_db
    }
    return render(request, 'goddesses/index.html', context=data)


def about(request):
    data = {
        'title': "About",
        'text': "About this site",
        'menu': menu,
    }
    return render(request, 'goddesses/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f"Post number {post_id}")


def add_post(request):
    return HttpResponse('Add post')


def contacts(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')