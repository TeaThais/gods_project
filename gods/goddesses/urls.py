from django.urls import path, register_converter

from . import views
from . import converters

# register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.GodsHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('goddess/<slug:post_slug>/', views.ShowPost.as_view(), name='goddess'),
    path('category/<slug:cat_slug>/', views.GoddessesCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.PostTags.as_view(), name='tag')
]