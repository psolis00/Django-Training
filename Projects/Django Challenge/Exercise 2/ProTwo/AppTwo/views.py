from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def users(request):
    ordered_users = User.objects.order_by("first_name")
    user_dict = {'users': ordered_users}
    return render(request, 'index/users.html', context=user_dict)


