from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse('The very first page')


def categories(request, cat_id):
    return HttpResponse(f"Categories <p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"Categories <p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"Archive for {year} year")


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')