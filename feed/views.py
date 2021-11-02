from django.shortcuts import render
from .models import Post

def index(request):
    """Displays the homepage of the user."""
    
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'feed/index.html', context)