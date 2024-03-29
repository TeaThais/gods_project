from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from goddesses.forms import AddPostForm, UploadFileForm
from goddesses.models import Goddesses, Category, TagPost, UploadFiles
from goddesses.utils import DataMixin


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


class GodsHome(DataMixin, ListView):
    template_name = 'goddesses/index.html'
    context_object_name = 'posts'
    title_page = "Gods & Goddesses"
    cat_selected = 0

    def get_queryset(self):
        return Goddesses.published.all().select_related('cat')

    # extra_context = {
    #     'title': "Gods & Goddesses",
    #     'menu': menu,
    #     'url': slugify("click here for the next page"),
    #     'cat_selected': 0,
    # }





# class GodsHome(TemplateView):
# template_name = 'goddesses/index.html'
# extra_context = {
#     'title': "Goddesses",
#     'menu': menu,
#     'posts': Goddesses.published.all().select_related('cat'),
#     'url': slugify("press here for the next page"),
#     'cat_selected': 0,
# }

# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def about(request):
    god_list = Goddesses.published.all()
    paginator = Paginator(god_list, 3)

    p_number = request.GET.get('page')
    page_obj = paginator.get_page(p_number)

    return render(request, 'goddesses/about.html', {'page_obj': page_obj})


 #  def about(request):
    # if request.method == 'POST':
    #     # handle_uploaded_file(request.FILES['file_upload'])
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # handle_uploaded_file(form.cleaned_data['file'])
    #         f = UploadFiles(file=form.cleaned_data['file'])
    #         f.save()
    # else:
    #     form = UploadFileForm()
    # data = {
    #     'title': "About",
    #     'text': "About this site",
    #     # 'menu': menu,
    #     'form': form
    # }
    # return render(request, 'goddesses/about.html', data)


# def show_post(request, post_slug):
#     post = get_object_or_404(Goddesses, slug=post_slug)
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 0
#     }
#     return render(request, 'goddesses/post.html', data)


class ShowPost(DataMixin, DetailView):
    # model = Goddesses
    template_name = 'goddesses/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_absolute_url'] = context['post'].get_edit_absolute_url()
        context['del_absolute_url'] = context['post'].get_del_absolute_url()
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Goddesses.published, slug=self.kwargs[self.slug_url_kwarg])


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


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    model = Goddesses
    fields = '__all__'
    template_name = 'goddesses/addpost.html'
    title_page = 'Add post'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        return super().form_valid(form)


class UpdatePost(DataMixin, UpdateView):
    model = Goddesses
    fields = '__all__'
    template_name = 'goddesses/addpost.html'
    title_page = 'Edit post'


class DeletePost(DeleteView):
    model = Goddesses
    fields = '__all__'
    success_url = reverse_lazy('home')


# class AddPost(View):
#     def get(self, request):
#         form = AddPostForm()
#         data = {
#             'menu': menu,
#             'title': 'Add post',
#             'form': form
#         }
#         return render(request, 'goddesses/addpost.html', data)
#
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#         data = {
#             'menu': menu,
#             'title': 'Add post',
#             'form': form
#         }
#         return render(request, 'goddesses/addpost.html', data)


@login_required
def contacts(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Goddesses.published.filter(cat_id=category.pk).select_related('cat')
#     data = {
#         'title': category.name,
#         'menu': menu,
#         'url': slugify("press here for the next page"),
#         'posts': posts,
#         'cat_selected': category.pk,
#     }
#     return render(request, 'goddesses/index.html', context=data)


class GoddessesCategory(DataMixin, ListView):
    template_name = 'goddesses/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Goddesses.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title='Category ' + cat.name,
                                      cat_selected=cat.pk)


class PostTags(DataMixin, ListView):
    template_name = 'goddesses/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Goddesses.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Tag ' + tags.slug)


# def tag_posts(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.post_tags.filter(is_published=Goddesses.Status.PUBLISHED).select_related('cat')
#     data = {
#         'title': tag.tag,
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': None,
#     }
#     return render(request, 'goddesses/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')
