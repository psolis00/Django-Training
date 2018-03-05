from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_help':"Help is on the way!",}
    return render(request, 'index/help.html', context=my_dict)

# Create your views here.
