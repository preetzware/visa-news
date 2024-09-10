from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import VisanewsArticle

# Create your views here.

class VisanewsList(generic.ListView):
    queryset = VisanewsArticle.objects.filter(status=1, category__name__icontains="Visa News") # Selects articles from Visa News category
    model = VisanewsArticle
    template_name = 'visanews/visanews_list.html'  # Template
    context_object_name = 'articles'  # Name of the context variable to use in the template
    paginate_by = 6 

def visanews_detail(request, slug):
    article = get_object_or_404(VisanewsArticle, slug=slug, status=1)
    return render(request, 'visanews/visanews_detail.html', {'article': article}) 


