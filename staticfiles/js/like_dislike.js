// Select the like button element from the DOM
const likeButton = document.getElementById("like-button");

// Select the dislike button element from the DOM
const dislikeButton = document.getElementById("dislike-button");

// Retrieve the article ID value from the hidden input field
const articleId = document.getElementById("article-id").value;

// Add an event listener to the like button
// When clicked, it will call the handleLikeDislike function with the "like" action
likeButton.addEventListener("click", () => {
    handleLikeDislike("like");
});

// Add an event listener to the dislike button
// When clicked, it will call the handleLikeDislike function with the "dislike" action
dislikeButton.addEventListener("click", () => {
    handleLikeDislike("dislike");
});

// Function to handle the like/dislike functionality
// It takes an "action" (either "like" or "dislike") and sends a POST request to the server
function handleLikeDislike(action) {
    // Use the Fetch API to send a POST request to the server
    fetch(`/like_article/${articleId}/`, { 
        method: "POST", // Define the method as POST
        headers: {
            'Content-Type': 'application/json', // Send JSON data
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
        },
        // Send the action (like or dislike) as part of the request body in JSON format
        body: JSON.stringify({ action: action })
    })
    .then(response => response.json()) // Parse the JSON response from the server
    .then(data => {
        // If the server response indicates success
        if (data.success) {
            // Update the like and dislike counts on the page
            document.getElementById("like-count").textContent = data.like_count;
            document.getElementById("dislike-count").textContent = data.dislike_count;
        } 
        // If there is an error in the response, display an alert with the error message
        else if (data.error) {
            alert(data.error);
        }
    })
    // If there's an error in the fetch request itself, log the error to the console
    .catch(error => {
        console.error("Error:", error);
    });
}

// Helper function to get CSRF token from browser cookies
// This is needed for Django to validate the POST request
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        // Split cookies by ';' and iterate to find the CSRF token
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // If the cookie starts with the name we're looking for, extract its value
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue; // Return the found CSRF token
}
