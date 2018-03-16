from django.shortcuts import render
from AppTwo.forms import UserForm
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def users(request):
    form = UserForm()
   
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR: FORM INVALID')
            
    return render(request, 'index/users.html', {'form':form})


