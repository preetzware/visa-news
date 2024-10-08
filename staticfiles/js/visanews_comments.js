/* global bootstrap */
const visanewsEditButtons = document.querySelectorAll('.visanews-btn-edit');
const visanewsDeleteButtons = document.querySelectorAll('.visanews-btn-delete');
const visanewsCommentText = document.getElementById('visanews-commentText');
const visanewsSubmitButton = document.getElementById('visanews-submitButton');
const visanewsCommentForm = document.getElementById('visanews-commentForm');
const visanewsDeleteModal = document.getElementById('visanewsDeleteModal');
const visanewsDeleteConfirm = document.getElementById('visanewsDeleteConfirm');

// Edit functionality for visanews comments
for (let button of visanewsEditButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentElement = document.getElementById(`visanews-comment${commentId}`);
        
        // Check if the commentElement exists
        if (commentElement) {
            let commentContent = commentElement.innerText; // Get the comment content
            
            // Find the textarea for the comment body using its class
            let visanewsCommentText = document.querySelector('.form-control[name="body"]');
            
            // Check if the textarea exists
            if (visanewsCommentText) {
                visanewsCommentText.value = commentContent; // Set the value of the textarea
                visanewsSubmitButton.innerText = "Update";
                visanewsCommentForm.setAttribute("action", `edit_comment/${commentId}/`);
            } else {
                console.error('Comment text input not found.');
            }
        } else {
            console.error('Comment element not found.');
        }
    });
}
  

// Delete functionality for visanews comments
for (let button of visanewsDeleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        visanewsDeleteConfirm.href = `delete_comment/${commentId}/`;
        
        // Show the modal using Bootstrap's Modal API
        const modalInstance = new bootstrap.Modal(visanewsDeleteModal);
        modalInstance.show();
    });
}

  