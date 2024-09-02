from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visa_articles")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='visa_articles')
    status = models.IntegerField(choices=STATUS, default=0)
    
    likes = models.ManyToManyField(User, related_name="article_likes", blank=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article_detail', kwargs={'slug': self.slug})

    class Category(models.Model):
        name = models.CharField(max_length=100)
        slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

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
        # Optional method if you want to return a general share URL or an icon class
        # Return a URL or a CSS class here for a generic share icon
        return "icon-class-name"  # Replace with your icon class or logic    
