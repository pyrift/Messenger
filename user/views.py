from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import authenticate, login

def singe_up_view(request):
    if request.method == 'POST':
        form = SingeUPForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect('login')
    else:
        form = SingeUPForm()
    return render(request, 'singeup.html', {'form': form})


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chat_list')

    return render(request, 'login.html')