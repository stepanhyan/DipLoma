const togglebtn = document.getElementById("toggleBtn")
togglebtn.addEventListener("click", function() {
    const navbar = document.querySelector('.navbar');
    navbar.classList.toggle("closed");
});

document.addEventListener('DOMContentLoaded', function () {
    const commentForm = document.querySelector('.comment-form');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    commentForm.addEventListener('submit', function (e) {
        e.preventDefault();
        console.log('submit button clicked');

        const formData = new FormData(this);
        const songId = this.getAttribute('data-song-id'); // Get the song ID
        formData.append('song_id', songId); // Append the song ID to the form data

        fetch('/comment/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Data received:', data);
            if (data.status === 'success') {
                // Append the new comment to the existing list
                const commentsList = document.querySelector('.comment-list');
                if (!commentsList) {
                    console.log("Comments list not found, check your DOM.");
                    return;
                }
                const commentElement = document.createElement('div');
                console.log('data need to find user ------->',data)
                commentElement.innerHTML = `User ${data.comment.user} - ${data.comment.text}`;
                commentsList.appendChild(commentElement); // Append the new comment

                // Clear the input field
                this.querySelector('.comment_input').value = '';
            } else {
                console.error(`Failed to post comment: ${data.message}`);
            }
        })
        .catch(error => console.error('Error:', error));
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const likeButtons = document.querySelectorAll('.like-btn');

        function updateLikeCount(button, likes, songId) {
            console.log('Updating like count:', likes); // Add this line for debugging
            const likeCount = button.parentElement.querySelector('.like-count');
            console.log('Like count element:', likeCount); // Add this line for debugging
            if (likeCount) {
               likeCount.textContent = likes;
            }
        }

        likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            console.log('Like button clicked');
            const songId = this.getAttribute('data-song-id');
            console.log(songId)

            fetch('/like/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken
                },
                body: `song_id=${encodeURIComponent(songId)}`  // Make sure to include song_id
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to like the song.');
                }
                return response.json();
            })
            .then(data => {
                console.log('Response data:', data);

                if (data.status === 'error') {
                    console.error('Error:', data.message);
                } else {
                    // Update the likes count on the client side
                    updateLikeCount(this, data.likes, songId);

                    // Toggle the visual state of the like button
                    const isLiked = data.is_liked;
                    if (isLiked) {
                        this.classList.add('liked');
                        console.log('User liked the song');
                    } else {
                        this.classList.remove('liked');
                        console.log('User unliked the song');
                    }
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

});


