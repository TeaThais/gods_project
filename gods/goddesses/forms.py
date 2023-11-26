from django import forms
from django.core.validators import MinLengthValidator

from .models import Category, Consort


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5,
                            error_messages={
                                'min_length': 'Must me more than 5 characters'
                            })
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message='5 characters minimum'),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not chosen')
    consort = forms.ModelChoiceField(queryset=Consort.objects.all(), required=False, empty_label='No consort')