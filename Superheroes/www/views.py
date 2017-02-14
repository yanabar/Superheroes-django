from django.shortcuts import render, redirect
from .models import Superhero
from .forms import SuperheroForm
from django.forms import model_to_dict
from django.core.urlresolvers import reverse # this would look up the url based up on the name, details and any arguments it needs, here is the slug

# Create your views here.
def index(request):
    # return a list of heroes and then to send this list to our templage we need to put in a dictionary
    heroes = Superhero.objects.all()
    return render(request, 'index.html', {'heroes':heroes})

def detail(request, slug):
    person = Superhero.objects.get(slug=slug)
    return render(request, 'detail.html', {'person':person})

def edit(request, slug):
    #person to pass into the form we are editing - like detail page
    person = Superhero.objects.get(slug=slug)
    #if rewuest is a post
    if (request.method == 'POST'):
        #Process form - this person we look from the slug field
        #update existing person with instance, like creating a new person
        form = SuperheroForm(data=request.POST, instance=person)
        if form.is_valid():
            form.save(commit = True) # True to save to DB /False: extra stuff to save on top of it
        return redirect(reverse('detail', args=[slug,]))
    else:
        #person needs to be in dictionary format! get all fields and map it to dictionary, populate fields
        person_dict = model_to_dict(person)
        form = SuperheroForm(person_dict)
        return render(request, 'edit.html', {'form':form})
