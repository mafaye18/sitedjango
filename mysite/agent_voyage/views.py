from django.shortcuts import render
from django .http import HttpResponse
from django.apps import apps

Destination = apps.get_model('agent_voyage', 'Destination')
Voyage = apps.get_model('agent_voyage', 'Voyage')
Excursion = apps.get_model('agent_voyage', 'Excursion')

posts = [
    {
        'author':'mafaye',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted' : 'August 27 , 2018'
    },
    {
        'author':'bamba',
        'title' : 'Blog post 2',
        'content': 'Second post content',
        'date_posted' : 'April 27 , 2018'
    }
]

def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'voyage/home.html',context)

def about(request):
    context={
                'destinations' : Destination.objects.all(),
                'voyages' : Voyage.objects.all()
            }
    return render(request, 'voyage/about.html',context )

def destination(request):

    return render(request, 'voyage/destination.html')

def voyage(request):
    
    return render(request, 'voyage/voyage.html')

def excursions(request):
    v = Voyage.objects.all()
    context={
        'voyage' : v}
    return render(request, 'voyage/excursions.html',context)