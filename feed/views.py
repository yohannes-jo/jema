from django.views.generic import TemplateView
from .models import Profile

class FeedPage(TemplateView):
    template_name = 'feed/home.html'
    model = Profile


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        
        return context