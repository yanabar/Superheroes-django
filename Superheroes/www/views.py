from django.shortcuts import render
from .models import Superhero

# Create your views here.
def index(request):
    # return a list of heroes and then to send this list to our templage we need to put in a dictionary
    heroes = Superhero.objects.all()
    return render(request, 'index.html', {'heroes':heroes})

def detail(request, slug):
    person = Superhero.objects.get(slug=slug)
    return render(request, 'detail.html', {'person':person})
