from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.models import User
from .models import Profile, Image
from .forms import editForm, createForm

def welcome(request):
   
    posts = Image.objects.all()
    
    return render(request, 'welcome.html', {'posts': posts})

def profile(request, user_id):
    user = request.user
    posts = Image.objects.filter(profile_user_id = user_id)
    
    # username = user.get_username
    # username = user.get_username()
    form = editForm()
    create_form = createForm()
    # if request.method == "POST":
    #     form = editForm(request.POST, request.FILES)
    #     create_form = createForm(request.POST, request.FILES)
    #     if form.is_valid() and create_form.is_valid():
    #         image = create_form.save(commit = False)
    #         profile = form.save(commit=False)
    #         profile.user = request.user
    #         image.profile_user = request.user
    #         profile.save()
    #         image.save()
            
    # else:
    #     form = editForm()
    #     create_form = createForm()

    try:
        current_user = request.user
        u = User.objects.get(id = user_id)
        profile = u.profile
        username = u.username
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'profile.html', {'form': form, 'posts': posts, 'create_form': create_form, 'profile': profile, 'username': username, 'user': user})


def create_post(request):
    form = createForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit = False)
        post.profile_user = request.user
        post.save()
        print("post has been created")
    return redirect('profile')


def update_profile(request):
    if request.method == 'POST':
        
        form = editForm(request.POST, request.FILES)
        if form.is_valid():
            usr = request.user
            Profile.objects.filter(user_id=usr.id).delete()
            # photo = request.POST['photo']
            # bio = request.POST['bio']
            # profile = Profile.objects.filter(user_id = request.user.id).update(photo = photo, bio = bio)
            profile = form.save(commit = False)
            profile.user = request.user
            profile.save()
            return redirect('profile')


def get_profile(request, user_id):
    user = request.user
    form = editForm()
    create_form = createForm()

    try:
        current_user = request.user
        u = User.objects.get(id = user_id)
        profile = u.profile
        username = u.username
    except Profile.DoesNotExist:
        profile = None
    
    return render(request, 'profile.html', {'form': form, 'posts': posts, 'create_form': create_form, 'profile': profile, 'username': username, 'user': user})

    





