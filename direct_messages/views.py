from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import MessageForm
from .models import Message
from profiles.models import Profile

@login_required
def messages(request, username):
    """Display all the messages sent between two users."""

    # Get the messages sent to and recieved by the user
    recieved = Message.objects.filter(reciever=Profile.objects.get(user=request.user))
    sent = Message.objects.filter(sender=Profile.objects.get(user=request.user))

    messages = recieved.union(sent).order_by('time')

    return render(request, 'direct_messages/inbox.html', {'messages': messages})

@login_required
def send_message(request, username):
    """Send a message to another user."""

    if request.method != 'POST':
        form = MessageForm()
    else:
        form = MessageForm(request.POST, request.FILES)

        if form.is_valid():
            # Add the sender
            current_message = form.save(commit=False)
            current_message.sender = Profile.objects.get(user=request.user)
            current_message.save()

            return redirect('direct_messages:inbox', username=request.user.username)

    return render(request, 'direct_messages/send_message.html', {'form': form})