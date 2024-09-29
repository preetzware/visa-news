from django.db.models import Q
from visanews.models import VisanewsArticle

def popular_articles(request):
    # Assuming 1 is the numeric value for 'published'
    published_status = 1  # Update this to match the value used in your model
    
    # Fetching the popular articles ordered by likes and then by updated_at
    popular_articles = (
        VisanewsArticle.objects
        .filter(status=published_status)  # Use the numeric value for published
        .order_by('-likes', '-updated_at')[:3]  # Limit to 3 articles
    )
    
    return {
        'popular_articles': popular_articles
    }
