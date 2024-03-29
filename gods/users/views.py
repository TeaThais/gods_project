from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from users.forms import LoginUserForm


# Create your views here.
# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})


class LoginUser(LoginView):
    # form_class = AuthenticationForm is default with username and password
    form_class = LoginUserForm
    template_name = 'users/login.html'
    # extra_context = {'title': ''}

    # def get_next_url(self, request):
    #     if 'next' in request.POST:
    #         return redirect(request.POST.get('add_post'))
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:logout'))


class LogoutUser(LogoutView):
    def get_success_url(self):
        return reverse_lazy('about')