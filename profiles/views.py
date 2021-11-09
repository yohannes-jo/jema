from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View

from notifications.models import Notification

from .models import Profile
from .forms import ProfileRegistrationForm

from feed.models import Post
from followers.models import Follower

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # if the user isn't submitting a form, give them a blank one
        form = UserCreationForm()
    else:
        # process the submitted form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('profiles:new_profile')
        
    # send a blank form (or resend an invalid form)
    context = {'form': form}

    return render(request, 'registration/register.html', context)

@login_required
def profile_registration(request):
    """Register a new profile based on given user."""
    if request.method != 'POST':
        # if the user isn't submitting a form, give them a blank one
        form = ProfileRegistrationForm()
    else:
        # process the submitted form
        form = ProfileRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            # Give the profile it's user first, then save
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()

            return redirect('feed:index')
        
    # send a blank form (or resend an invalid form)
    context = {'form': form}

    return render(request, 'profiles/new_profile.html', context)

@login_required
def detail(request, username):
    """Return the information of the currently logged-in user."""
    current_profile = Profile.objects.get(user=User.objects.get(username=username))
    post_count = Post.objects.filter(author=User.objects.get(username=username)).count()
    follower_count = Follower.objects.filter(following=User.objects.get(username=username)).count()
    you_follow = Follower.objects.filter(follower=request.user, following=current_profile.user).exists()

    context = {'profile': current_profile, 'post_count': post_count, 'follower_count': follower_count, 'you_follow': you_follow}

    return render(request, 'profiles/detail.html', context)

@login_required
def edit_profile(request, username):
    """Edit the information of the currently logged-in user."""
    
    return render(request, 'profiles/edit_profile.html', {})
            
@login_required
def follow(request, username):
    """Follow a given user."""
    data = request.POST.dict()

    if 'action' not in data or 'username' not in data:
        return HttpResponseBadRequest('Missing data')

    other_user = User.objects.get(username=data['username'])
    
    if data['action'] == 'follow':
        follow, created= Follower.objects.get_or_create(
            follower = request.user,
            following = other_user,
        )
        follow.save()
        
        followed_person = follow.following

        notification = Notification.objects.create(
            notified_to = Profile.objects.get(user=followed_person),
            notifier = Profile.objects.get(user=request.user),
        )
        notification.caption = f"Hey! {notification.notifier.user.username} just started following you."

        notification.save()

    else:
        try:
            follower = Follower.objects.get(
                follower=request.user,
                following=other_user,
            )
        except Follower.DoesNotExist:
            follower = None

        if follower:
            follower.delete()
        
    return JsonResponse({
        'success': True,
        'wording': 'Unfollow' if data['action'] == 'follow' else 'Follow'
    })