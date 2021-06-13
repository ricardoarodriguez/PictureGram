### Picturegram views. ###

# Django
from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    ### Return a Gretting ###

    return HttpResponse('System Date {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def hi(request):
    ### Hi ###
    print(request)
    return HttpResponse('Hi')