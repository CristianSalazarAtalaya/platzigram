"""port views"""

#from django.shortcuts import render

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Cristian Salazar',
        'user': 'Csalazaraz',
        'timestamp': datetime.now().strftime('%b %dth. %Y -%H:%M hrs'),
        'picture':'https://picsum.photos/200/200?image=1036'
    },
    {
        'name': 'Via lactea',
        'user': 'C Vander',
        'timestamp': datetime.now().strftime('%b %dth. %Y -%H:%M hrs'),
        'picture':'https://picsum.photos/200/200?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'mirme',
        'timestamp': datetime.now().strftime('%b %dth. %Y -%H:%M hrs'),
        'picture':'https://picsum.photos/200/200?image=1076'
    },
]

# Create your views here.

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p>{user}</p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
