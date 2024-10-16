from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm
from django.views.decorators.http import require_POST
import json
from visanews.models import VisanewsArticle


# Create your views here.

class ArticleList(generic.ListView):
    queryset = Article.objects.all()
    template_name = "visa_app/index.html"
    paginate_by = 6


def article_detail(request, slug):
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    like_count = article.number_of_likes()
    dislike_count = article.number_of_dislikes()
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank You! Your comment is awaiting approval.'
            )

    comment_form = CommentForm()

    return render(request, "visa_app/article_detail.html", {
        "article": article,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "like_count": like_count,
        "dislike_count": dislike_count,
    })


def index_view(request):
    latest_articles = Article.objects.order_by('-published_at')[:3]
    featured_article = Article.objects.order_by('-published_at')[3]
    other_articles = Article.objects.order_by('-published_at')[4:7]

    context = {
        'latest_articles': latest_articles,
        'featured_article': featured_article,
        'other_articles': other_articles,
    }
    return render(request, 'visa_app/index.html', context)


def search_view(request):
    """
    View for users to be able to search articles by matching words
    in the title, excerpt, and category fields of the articles.
    Including all these fields by using Django's Q objects that
    will allow to perform complex queries with OR conditions.
    """
    query = request.GET.get('query')
    articles = Article.objects.filter(title__icontains=query)
    visanews_articles = VisanewsArticle.objects.filter(title__icontains=query)

    context = {
        'articles': articles,
        'visanews_articles': visanews_articles,
        'query': query,
    }

    return render(request, 'visa_app/search_results.html', context)


@require_POST
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    action = json.loads(request.body).get('action')

    if action == 'like':
        article.likes.add(request.user)
        article.dislikes.remove(request.user)
    elif action == 'dislike':
        article.dislikes.add(request.user)
        article.likes.remove(request.user)

    return JsonResponse({
        'success': True,
        'like_count': article.likes.count(),
        'dislike_count': article.dislikes.count(),
    })


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    """
    if request.method == "POST":
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment Updated and awaiting approval!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comment.
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))


def forgot_password(request):
    return render(request, 'visa_app/forgotpassword.html')
