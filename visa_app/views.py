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

def index_view(request):
    latest_articles = Article.objects.all().order_by('-published_at')[:3]  # Latest 3 articles for the carousel
    other_articles = Article.objects.all().order_by('-published_at')[3:9]  # The rest of the articles for cards
    return render(request, 'visa_app/index.html', {
        'latest_articles': latest_articles,
        'other_articles': other_articles,}) 

def search_view(request):
    query = request.GET.get('query')
    search_results = Article.objects.filter(title__icontains=query)  # Adjust to match your model
    return render(request, 'visa_app/search_results.html', {'results': search_results, 'query': query}) 