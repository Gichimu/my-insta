from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Image
from .forms import editForm

def welcome(request):
    return render(request, 'welcome.html')

def profile(request):
    if request.method == "POST":
        form = editForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = editForm()

    try:
        current_user = request.user
        profile = Profile.objects.filter(id=current_user.id)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'form': form, 'profile': profile})




