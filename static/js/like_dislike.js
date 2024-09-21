document.getElementById('like-button').addEventListener('click', function() {
    const articleId = '{{ article.id }}';  // Ensure this is in the context of your article_detail.html
    fetch('/like-article/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ article_id: articleId, action: 'like' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('like-count').innerText = data.likes;
        }
    });
});

// Similarly for the dislike button
document.getElementById('dislike-button').addEventListener('click', function() {
    const articleId = '{{ article.id }}';  // Ensure this is in the context of your article_detail.html
    fetch('/like-article/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ article_id: articleId, action: 'dislike' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('like-count').innerText = data.likes;
        }
    });
});
