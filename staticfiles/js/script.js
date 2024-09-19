document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.getElementById('like-button');
    const dislikeButton = document.getElementById('dislike-button');
    const likeCountSpan = document.getElementById('like-count');
    const dislikeCountSpan = document.getElementById('dislike-count');

    // Add event listeners to buttons
    if (likeButton && dislikeButton) {
        likeButton.addEventListener('click', function() {
            // Perform AJAX request to update like count
            fetch('/like/', {
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
                    likeCountSpan.textContent = data.likes;
                    // Optionally, change button style to active
                    likeButton.classList.add('active');
                }
            });
        });

        dislikeButton.addEventListener('click', function() {
            // Perform AJAX request to update dislike count
            fetch('/dislike/', {
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
                    dislikeCountSpan.textContent = data.dislikes;
                    // Optionally, change button style to active
                    dislikeButton.classList.add('active');
                }
            });
        });
    }

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
