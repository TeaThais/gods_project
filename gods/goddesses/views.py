from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string


menu = ['About', 'Add article', 'Contacts', 'Login']


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


def categories(request, cat_id):
    return HttpResponse(f"Categories <p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"Categories <p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        # raise Http404()
        # return redirect('home', permanent=True)
        uri = reverse('categories', args=('egypt', ))    # uri will have 'cats/egypt/'
        return redirect(uri)
    return HttpResponse(f"Archive for {year} year")


def about(request):
    data = {
        'title': "About",
        'text': "About this site",
        'menu': menu,
    }
    return render(request, 'goddesses/about.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')