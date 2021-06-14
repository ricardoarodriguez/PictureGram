### Posts views. ###

### Django 
from django import http
## from django.http import HttpResponse
from django.shortcuts import render ### funcion que toma un request 
from datetime import datetime 

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortés',
            'picture': 'https://picsum.photos/200/200/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/200/200/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'title': 'Nuevo Auditorio',
        'user': {
            'name':'Uriel (Thespianartist)',
            'picture': 'https://picsum.photos/200/200/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1076',
    },
]

def list_post(request):
    return render(request, 'feed.html', {'posts':posts})
                ### petición, nombre del Template, contexto 

'''
def list_post(request):
    ### List existing posts. This is used with HttpResponse ###
    content = []
    for post in posts:
        content.append("""  
            <p><strong>{name}</strong></p>
            <p><strong>{user} - <i>{timestamp}</i></strong></p>
            <figure><img src="{picture}"</figure>
        """.format(**post))  ### ---> Desempaquetador de Diccionarios  ### ### .append itera objeto posts y agrega elementos a contect ###
    return HttpResponse('<br>'.join(content)) ### Unir elementos y separar por tag de espacio 
'''