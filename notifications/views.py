from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Notification
from profiles.models import Profile

@login_required
def notification(request):
    """Show all the notifications recieved from another user."""

    if Notification.objects.filter(notified_to=Profile.objects.get(user=request.user)):
        notifications = Notification.objects.filter(notified_to=Profile.objects.get(user=request.user)).order_by('-time')
        return render(request, 'notifications/page.html', {'notifications': notifications})

    return render(request, 'notifications/page.html')
