from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import hashlib


# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def sha_upload_page(request):
    if request.method == 'POST':
        name = request.FILES['uploaded_file'].name
        h = hashlib.sha256()
        h.update(request.FILES['uploaded_file'].read())
        # return the hex representation of digest
        print(h.hexdigest())
    return render(request, "parakeet/sha-upload.html", {'digestsha256': h.hexdigest(), 'namefile': name})