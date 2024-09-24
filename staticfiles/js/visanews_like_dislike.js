(function () {
    const likesButton = document.getElementById("likes-button");
    const dislikesButton = document.getElementById("dislikes-button");
    const articleId = document.getElementById("articles-id").value;

    likesButton.addEventListener("click", () => {
        handleVisanewsLikeDislike("like");
    });

    dislikesButton.addEventListener("click", () => {
        handleVisanewsLikeDislike("dislike");
    });

    function handleVisanewsLikeDislike(action) {
        fetch(`/visanews/like_article/${articleId}/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getVisanewsCookie('csrftoken')
            },
            body: JSON.stringify({ action: action })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("likes-count").textContent = data.like_count;
                document.getElementById("dislikes-count").textContent = data.dislike_count;
            } else if (data.error) {
                alert(data.error);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }

    function getVisanewsCookie(name) {
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
})();
