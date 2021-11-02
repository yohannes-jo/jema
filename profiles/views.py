from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import ProfileRegistrationForm

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

def profileRegistration(request):
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

