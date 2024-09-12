from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()
    return render(request, "visa_app/article_detail.html", {
        "article": article,
        "comments": comments,
        "comment_count": comment_count,
    })  

def index_view(request):
    latest_articles = Article.objects.all().order_by('-published_at')[:3]  # Latest 3 articles for the carousel
    other_articles = Article.objects.all().order_by('-published_at')[3:9]  # The rest of the articles for cards
    return render(request, 'visa_app/index.html', {
        'latest_articles': latest_articles,
        'other_articles': other_articles,}) 

def search_view(request):
    """
   View for users to be able to search articles by matching words in the title, excerpt, and category fields of the articles. 
   Including all these fields by using Django's Q objects that will allow to perform complex queries with OR conditions.
    """
    query = request.GET.get('query')
    if query:
        search_results = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(excerpt__icontains=query) | 
            Q(category__name__icontains=query)  # Assuming category has a `name` field
        ).distinct()  # `distinct()` ensures no duplicate results
    else:
        search_results = Article.objects.none()  # Return no results if the query is empty
    return render(request, 'visa_app/search_results.html', {'results': search_results, 'query': query}) 
    
    """
    Q Objects: Django's Q objects is used to construct complex queries that check if the search term 
    (query) is found in any of the title, excerpt, or category.name fields. 
    icontains Lookup: The icontains lookup is used to perform case-insensitive partial matching. 
    distinct() Method: This ensures that if an article matches in multiple fields, it only appears 
    once in the search results.
    """