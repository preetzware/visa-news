from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import VisanewsArticle, Comment
from .forms import CommentForm
from django.views.decorators.http import require_POST
import json


# Visanews Article List View
class VisanewsList(generic.ListView):
    queryset = VisanewsArticle.objects.filter(
        status=1, category__name__icontains="Visa News")
    model = VisanewsArticle
    context_object_name = 'articles'
    template_name = 'visanews/visanews_list.html'
    paginate_by = 6


# Visanews Article Detail View
def visanews_detail(request, slug):
    article = get_object_or_404(
        VisanewsArticle.objects.filter(status=1), slug=slug)
    like_count = article.number_of_likes()
    dislike_count = article.number_of_dislikes()
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            messages.success(
                request, 'Thank you! Your comment is awaiting approval.')
        else:
            messages.error(
                request,
                'There was an error with your comment. Please try again.')

        comment_form = CommentForm()

    return render(request, "visanews/visanews_detail.html", {
        "article": article,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "like_count": like_count,
        "dislike_count": dislike_count,
    })

# Edit Comment View for Visanews


def comment_edit(request, slug, comment_id):

    if request.method == "POST":

        article = get_object_or_404(VisanewsArticle, slug=slug, status=1)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

    if comment_form.is_valid() and comment.user == request.user:
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.approved = False
        comment.save()
        messages.success(request, 'Comment Updated and awaiting approval!')
    else:
        messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('visanews_detail', args=[slug]))


# Delete Comment View for Visanews
def comment_delete(request, slug, comment_id):
    article = get_object_or_404(
     VisanewsArticle.objects.filter(status=1),
     slug=slug
    )
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('visanews_detail', args=[slug]))


# Search View for Visanews
def visanews_search_view(request):
    query = request.GET.get('query')
    if query:
        search_results = VisanewsArticle.objects.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    else:
        search_results = VisanewsArticle.objects.none()

    return render(
        request,
        'visanews/visanews_search_results.html',
        {'results': search_results, 'query': query}
    )


# Like and Dislike Buttons
@require_POST
def like_article(request, article_id):
    article = get_object_or_404(VisanewsArticle, id=article_id)
    action = json.loads(request.body).get('action')

    if action == 'like':
        article.likes.add(request.user)

    if request.user in article.dislikes.all():
        article.dislikes.remove(request.user)


    elif action == 'dislike':
        article.dislikes.add(request.user)

    if request.user in article.likes.all():
        article.likes.remove(request.user)

    return JsonResponse({
        'success': True,
        'like_count': article.likes.count(),
        'dislike_count': article.dislikes.count(),
    })
