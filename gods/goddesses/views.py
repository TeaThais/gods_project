from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    # text = render_to_string('goddesses/index.html')
    # return HttpResponse(text)
    return render(request, 'goddesses/index.html')


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
    return render(request, 'goddesses/about.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')