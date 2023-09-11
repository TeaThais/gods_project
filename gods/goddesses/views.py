from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('The very first page')


def categories(request, cat_id):
    return HttpResponse(f"Categories <p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"Categories <p>slug: {cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"Archive for {year} year")