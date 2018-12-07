from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """register new user"""
    if request.method != 'POST':
        # show empty form
        form = UserCreationForm() #1
    else:
        # process form after user input
        form = UserCreationForm(data=request.POST) #2

        if form.is_valid(): #3
            new_user = form.save() #4
            # user login and redirect to index
            authenticated_user = authenticate(username=new_user.username, #5
                                              password=request.POST['password1'])
            login(request, authenticated_user) #6
            return HttpResponseRedirect(reverse('learning_logs:index')) #7

    context = {'form': form}
    return render(request, 'users/register.html', context)
