from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here
# we handle the registration logic.
# a user can register in the site
def register(request):
    if request.method == 'post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form':form})
        
# we handle the login logic
# a user can login in the site
def login(request):
    if request.methid == 'post':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user
            login(request, user)
            return redirect('list')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})
            
# use logout logic
# a user can logout from the website
def user_logout(request):
    logout(request)
    return redirect('login')


