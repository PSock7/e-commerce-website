from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.



def register(request):
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request,'registration/register.html', {'form': form  })

@login_required

def profile(request):
    return render(request, 'registration/profile.html')