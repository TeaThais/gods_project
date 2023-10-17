from django.urls import path, register_converter

from . import views
from . import converters

# register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpost/', views.add_post, name='add_post'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('goddess/<slug:post_slug>/', views.show_post, name='goddess'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.tag_posts, name='tag')
]