from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article

# Create your views here.

class ArticleList(generic.ListView):
    queryset = Article.objects.all()
    template_name = "visa_app/index.html"
    paginate_by = 6

def article_detail(request, slug):
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    return render(request, "visa_app/article_detail.html", {"article": article},)    

def search_view(request):
    query = request.GET.get('query')
    search_results = Article.objects.filter(title__icontains=query)  # Adjust to match your model
    return render(request, 'visa_app/search_results.html', {'results': search_results, 'query': query}) 