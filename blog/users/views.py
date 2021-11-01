from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='raia')
            user.groups.add(group)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request, 'users/register.html', context)
