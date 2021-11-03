from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Post
from .forms import PostForm

def index(request):
    """Displays the homepage of the user.""" 
    posts = Post.objects.order_by('-date_added').filter(author=request.user) # TODO: add followed people too
    context = {'posts': posts}

    return render(request, 'feed/index.html', context)

def explore(request):
    """Displays all posts."""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'feed/explore.html', context)

@login_required
def add_post(request):
    """Add a new post to the feed."""
    if request.method != 'POST':
        # If it is an initial request, give a blank form
        form = PostForm()
    else:
        # Submit the form for validation
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            # Give the post an author first, then save
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('feed:index')
    
    # If it's an initial request or an invalid form, redirect to the same page
    return render(request, 'feed/add_post.html', {'form': form})