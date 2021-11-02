from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new account."""
    if request.method != 'POST':
        # if the user isn't submitting a form, give them a blank one
        form = UserCreationForm()
    else:
        # process the submitted form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('feed:index')
        
    # send a blank form (or resend an invalid form)
    context = {'form': form}

    return render(request, 'registration/register.html', context)