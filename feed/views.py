from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Comment, Post
from .forms import CommentForm, PostForm

from followers.models import Follower
from profiles.models import Profile
from notifications.models import Notification

def index(request):
    """Displays the homepage of the user.""" 
    if request.user.is_authenticated:
        posts = Post.objects.order_by('-date_added').filter(author=request.user) # TODO: add followed people too
        context = {'posts': posts}
        return render(request, 'feed/index.html', context)
    
    return render(request, 'feed/index.html')

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

            # Send a notification to all the user's followers
            followers = Follower.objects.filter(following=request.user)

            for relationship in followers.iterator():
                notification = Notification.objects.create()
                notification.notified_to = Profile.objects.get(user=relationship.follower)
                notification.notifier = Profile.objects.get(user=request.user)

                notification.caption = f"Hey! {notification.notifier.user.username} just created a new post."

                notification.save()

            return redirect('feed:index')
    
    # If it's an initial request or an invalid form, redirect to the same page
    return render(request, 'feed/add_post.html', {'form': form})

@login_required
def post(request, post_id):
    """Show a detailed view of a post, along with the ability to see and add comments."""
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=Post.objects.get(id=post_id))

    if request.method != 'POST':
        # post an empty form
        form = CommentForm()
    else:
        # submit form for validation
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            # Give the comment the related post and the author first, then save
            comment = form.save(commit=False)
            comment.by = Profile.objects.get(user=request.user)
            comment.post = post

            comment.save()

            # send a notification to all the user's followers
            followers = Follower.objects.filter(following=request.user)

            for relationship in followers.iterator():
                notification = Notification.objects.create()
                notification.notified_to = Profile.objects.get(user=relationship.follower)
                notification.notifier = Profile.objects.get(user=request.user)

                notification.caption = f"Hey! {notification.notifier.user.username} just commented on {notification.notified_to.user.username}'s post: {comment.text}."

                notification.save()

            return redirect('feed:post', post_id=post_id)

    # If it's an initial request or an invalid form, redirect to the same page
    context = {'form': form, 'post': post, 'comments': comments}

    return render(request, 'feed/post.html', context)


    