from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.

class ArticleList(generic.ListView):
    queryset = Article.objects.all()
    template_name = "visa_app/index.html"
    paginate_by = 6

def search_view(request):
    query = request.GET.get('query')
    search_results = Article.objects.filter(title__icontains=query)  # Adjust to match your model
    return render(request, 'visa_app/search_results.html', {'results': search_results, 'query': query}) 