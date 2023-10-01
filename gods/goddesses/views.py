from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add post', 'url_name': 'add_post'},
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Login', 'url_name': 'login'}
]


data_db = [
    {'id': 1, 'name': 'Isis', 'content': '''Isis was a major goddess in ancient Egyptian religion whose worship spread
     throughout the Greco-Roman world. Isis was first mentioned in the Old Kingdom as one of the main characters of 
     the Osiris myth, in which she resurrects her slain brother and husband, the divine king Osiris, 
     and produces and protects his heir, Horus. She was believed to help the dead enter the afterlife 
     as she had helped Osiris, and she was considered the divine mother of the pharaoh, who was likened to Horus. 
     Her maternal aid was invoked in healing spells to benefit ordinary people. Originally, she played a limited role
      in royal rituals and temple rites, although she was more prominent in funerary practices and magical texts. 
      She was usually portrayed in art as a human woman wearing a throne-like hieroglyph on her head. 
      During the New Kingdom (c. 1550 – c. 1070 BCE), as she took on traits that originally belonged to Hathor, 
      the preeminent goddess of earlier times, Isis was portrayed wearing Hathor's headdress: a sun disk between the
        horns of a cow. ''',
     'is_published': True},

    {'id': 2, 'name': 'Aphrodite', 'content': 'Greek goddess', 'is_published': False},

    {'id': 3, 'name': 'Hathor', 'content': '''Hathor was a major goddess in ancient Egyptian religion who played 
    a wide variety of roles. As a sky deity, she was the mother or consort of the sky god Horus and the sun god Ra, 
    both of whom were connected with kingship, and thus she was the symbolic mother of their earthly representatives, 
    the pharaohs. She was one of several goddesses who acted as the Eye of Ra, Ra's feminine counterpart, 
    and in this form she had a vengeful aspect that protected him from his enemies. Her beneficent side 
    represented music, dance, joy, love, sexuality, and maternal care, and she acted as the consort 
    of several male deities and the mother of their sons. These two aspects of the goddess exemplified 
    the Egyptian conception of femininity. Hathor crossed boundaries between worlds, helping deceased souls 
    in the transition to the afterlife. ''',
     'is_published': True},

    {'id': 4, 'name': 'Astarte', 'content': '''Astarte is the Hellenized form 
    of the Ancient Near Eastern goddess ʿAṯtart. ʿAṯtart was the Northwest Semitic equivalent 
    of the East Semitic goddess Ishtar.
    Astarte was worshipped from the Bronze Age through classical antiquity, and her name is particularly associated
     with her worship in the ancient Levant among the Canaanites and Phoenicians, though she was originally associated
      with Amorite cities like Ugarit and Emar, as well as Mari and Ebla.[6] She was also celebrated in Egypt, 
      especially during the reign of the Ramessides, following the importation of foreign cults there. 
      Phoenicians introduced her cult in their colonies on the Iberian Peninsula. ''',
     'is_published': True},
]


def index(request):
    # text = render_to_string('goddesses/index.html')
    # return HttpResponse(text)
    data = {
        'title': "Goddesses",
        'menu': menu,
        'url': slugify("press here for the next page"),
        'posts': data_db
    }
    return render(request, 'goddesses/index.html', context=data)


def about(request):
    data = {
        'title': "About",
        'text': "About this site",
        'menu': menu,
    }
    return render(request, 'goddesses/about.html', data)


def show_post(request, post_id):
    return HttpResponse(f"Post number {post_id}")


def add_post(request):
    return HttpResponse('Add post')


def contacts(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound('Nothing was found here')