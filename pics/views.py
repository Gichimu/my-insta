from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, get_user_model
from .models import Profile, Image
from .forms import editForm

def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    model = get_user_model()
    username = model.username
    user = get_user(request)
    # username = user.get_username
    username = user.get_username()
    if request.method == "POST":
        form = editForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = editForm()

    # try:
    #     current_user = request.user
    #     profile = Profile.objects.filter(id=current_user.id)
    # except Profile.DoesNotExist:
    #     profile = None

    return render(request, 'profile.html', {'form': form, 'profile': profile, 'username': username, 'user': user})




