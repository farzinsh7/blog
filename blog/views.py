from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class BlogListView(ListView):
    queryset = models.Blog.objects.published()
    model = models.Blog
    template_name = 'blog_list.html'
    context_object_name = 'blog'
    paginate_by = 9


class BlogDetailView(DetailView):
    model = models.Blog
    context_object_name = 'blog'
    queryset = models.Blog.objects.published()
    template_name = 'blog_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = models.Blog.objects.published()[:3]
        context['category'] = models.Category.objects.filter(status=True)
        context['tags'] = models.Tags.objects.filter(status=True)
        return context