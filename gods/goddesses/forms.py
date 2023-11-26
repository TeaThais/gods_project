from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from .models import Category, Consort, Goddesses


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Not chosen')
    consort = forms.ModelChoiceField(queryset=Consort.objects.all(), required=False, empty_label='No consort')

    class Meta:
        model = Goddesses
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 15:
            raise ValidationError('Title is longer than 15 characters')
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')

    # title = forms.CharField(max_length=255, min_length=5,
    #                         error_messages={
    #                             'min_length': 'Must me more than 5 characters'
    #                         })
    # slug = forms.SlugField(max_length=255, label='URL',
    #                        validators=[
    #                            MinLengthValidator(5, message='5 characters minimum'),
    #                        ])
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    # is_published = forms.BooleanField(required=False, initial=True)
