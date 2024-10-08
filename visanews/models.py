from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class VisanewsArticle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="visanews_author"
    )
    visanews_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='visanews_articles'
    )
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
     User, related_name="visanews_likes", blank=True
    )
    dislikes = models.ManyToManyField(
     User, related_name="visanews_dislikes", blank=True
    )

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):
        return reverse('visanews_detail', kwargs={'slug': self.slug})

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()

    # Methods to generate social media share URLs
    def get_facebook_share_url(self):
        base_url = "https://www.facebook.com/sharer/sharer.php?u="
        return f"{base_url}{self.get_absolute_url()}"

    def get_twitter_share_url(self):
        base_url = "https://twitter.com/intent/tweet?url="
        return f"{base_url}{self.get_absolute_url()}&text={self.title}"

    def get_linkedin_share_url(self):
        base_url = "https://www.linkedin.com/sharing/share-offsite/?url="
        return f"{base_url}{self.get_absolute_url()}"

    def get_whatsapp_share_url(self):
        base_url = "https://api.whatsapp.com/send?text="
        return f"{base_url}{self.title} {self.get_absolute_url()}"

    def get_share_icon(self):
        return "icon-class-name"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(
        VisanewsArticle, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='visanews_comments'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey(
     'self',
     on_delete=models.CASCADE,
     null=True,
     blank=True,
     related_name='replies'
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.user} on {self.article.title}"
