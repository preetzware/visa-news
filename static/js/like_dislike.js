const likeButton = document.getElementById("like-button");
const dislikeButton = document.getElementById("dislike-button");

const articleId = document.getElementById("article-id").value;  // Assuming you have articleId from a hidden input

likeButton.addEventListener("click", () => {
    handleLikeDislike("like");
});

dislikeButton.addEventListener("click", () => {
    handleLikeDislike("dislike");
});

function handleLikeDislike(action) {
    fetch(`/like_article/${articleId}/`, {  // Updated to match the new URL pattern with articleId
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Ensure you get the CSRF token
        },
        body: JSON.stringify({ action: action })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the like and dislike counts
            document.getElementById("like-count").textContent = data.like_count;
            document.getElementById("dislike-count").textContent = data.dislike_count;
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

// Helper function to get CSRF token
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
