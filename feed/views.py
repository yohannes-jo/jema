from django.shortcuts import render

def index(request):
    """Displays the homepage of the user."""
    return render(request, 'feed/index.html')