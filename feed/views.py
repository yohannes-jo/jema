from django.views.generic import TemplateView
from .models import Post

class FeedPage(TemplateView):
    template_name = 'feed/home.html'
    model = Post


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        
        return context