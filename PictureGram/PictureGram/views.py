### Picturegram views. ###

# Django
from django.http import HttpResponse, response
from datetime import datetime
import json 

def hello_world(request):
    ### Return a Gretting ###
    return HttpResponse('System Date {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))
  
def sorted_integers(request):
    ### Return a Json response with sorted integers ###
    ## import pdb; pdb.set_trace() Debugger en consola
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted sucessfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json') ###HttpResponse(str(numbers))

def sign_in_validation(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allow here '.format(name)
    else:
        message = 'Hello {}, Welcome you Picturegram '.format(name)
    return HttpResponse(message)
