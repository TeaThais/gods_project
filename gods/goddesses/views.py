from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from goddesses.forms import AddPostForm, UploadFileForm
from goddesses.models import Goddesses, Category, TagPost, UploadFiles

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add post', 'url_name': 'add_post'},
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Login', 'url_name': 'login'}
]


# def index(request):
#     posts = Goddesses.published.all().select_related('cat')
#     data = {
#         'title': "Goddesses",
#         'menu': menu,
#         'posts': posts,
#         'url': slugify("press here for the next page"),
#         'cat_selected': 0,
#     }
#     return render(request, 'goddesses/index.html', context=data)


class GodsHome(TemplateView):
    template_name = 'goddesses/index.html'
    extra_context = {
        'title': "Goddesses",
        'menu': menu,
        'posts': Goddesses.published.all().select_related('cat'),
        'url': slugify("press here for the next page"),
        'cat_selected': 0,
    }

# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':
        # handle_uploaded_file(request.FILES['file_upload'])
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            f = UploadFiles(file=form.cleaned_data['file'])
            f.save()
    else:
        form = UploadFileForm()
    data = {
        'title': "About",
        'text': "About this site",
        'menu': menu,
        'form': form
    }
    return render(request, 'goddesses/about.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Goddesses, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 0
    }
    return render(request, 'goddesses/post.html', data)


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     data = {
#         'menu': menu,
#         'title': 'Add post',
#         'form': form
#     }
#     return render(request, 'goddesses/addpost.html', data)


class AddPost(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'menu': menu,
            'title': 'Add post',
            'form': form
        }
        return render(request, 'goddesses/addpost.html', data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        data = {
            'menu': menu,
            'title': 'Add post',
            'form': form
        }
        return render(request, 'goddesses/addpost.html', data)


def contacts(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Goddesses.published.filter(cat_id=category.pk).select_related('cat')
    data = {
        'title': category.name,
        'menu': menu,
        'url': slugify("press here for the next page"),
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'goddesses/index.html', context=data)


def tag_posts(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.post_tags.filter(is_published=Goddesses.Status.PUBLISHED).select_related('cat')
    data = {
        'title': tag.tag,
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'goddesses/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')