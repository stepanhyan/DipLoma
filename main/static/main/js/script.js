const togglebtn = document.getElementById("toggleBtn")
togglebtn.addEventListener("click", function() {
    const navbar = document.querySelector('.navbar');
    navbar.classList.toggle("closed");
});

// const profileNav = document.getElementById("profile")
// const loginNav = document.getElementById("login")
// const signupNav = document.getElementById("signup")
//
// profileNav.addEventListener('mouseenter', (e)=>{
//     console.log('mouse enter')
//     loginNav.style.display = 'block';
//     signupNav.style.display = 'block';
// })
// profileNav.addEventListener('mouseleave', (e)=>{
//     console.log('mouse leave')
//     loginNav.style.display = 'none';
//     signupNav.style.display = 'none';
// })


// document.addEventListener('DOMContentLoaded', function () {
//     const commentForm = document.querySelector('.comment-form');
//
//     commentForm.addEventListener('submit', function (e) {
//         e.preventDefault();
//
//         const formData = new FormData(this);
//
//         fetch('/comment/', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 // Update the comments section with the new comment
//                 const commentsDiv = document.querySelector('.comments');
//                 const p = document.createElement('p');
//                 p.textContent = `${data.comment.user} - ${data.comment.text}`;
//                 commentsDiv.appendChild(p);
//
//                 // Clear the input field
//                 this.querySelector('.comment_input').value = '';
//             } else {
//                 alert('Failed to post comment.');
//             }
//         })
//         .catch(error => console.error('Error:', error));
//     });
// });


// document.addEventListener('DOMContentLoaded', function () {
//     const commentForm = document.forms['comment-form'];  // Assuming the form has a name attribute
//
//     if (commentForm) {
//         const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//
//         commentForm.addEventListener('submit', function (e) {
//             e.preventDefault();
//             console.log('submit button clicked')
//
//             const formData = new FormData(this);
//             // console.log(formData)
//
//             fetch('/comment/', {
//                 method: 'POST',
//                 headers: {
//                     'X-CSRFToken': csrfToken
//                 },
//                 body: formData
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status === 'success') {
//                     // Append the new comment to the existing list
//                     const commentsList = document.querySelector('.comments');
//                     const p = document.createElement('p');
//                     p.textContent = `${data.comment.user} - ${data.comment.text}`;
//                     commentsList.appendChild(p);
//
//                     // Clear the input field
//                     this.querySelector('.comment_input').value = '';
//                 } else {
//                     console.log(`Failed to post comment: ${data.message}`);
//                 }
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     } else {
//         console.error('Comment form not found');
//     }
// });

// document.addEventListener('DOMContentLoaded', function () {
//     const commentForm = document.querySelector('.comment-form');
//
//     if (commentForm) {
//         commentForm.addEventListener('submit', function (e) {
//             e.preventDefault();
//             console.log('submit button clicked');
//
//             const formData = new FormData(this);
//
//             fetch('/comment/', {
//                 method: 'POST',
//                 body: formData
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status === 'success') {
//                     console.log('Comment posted successfully');
//                 } else {
//                     console.log(`Failed to post comment: ${data.message}`);
//                 }
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     } else {
//         console.error('Comment form not found');
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    const commentForm = document.querySelector('.comment-form');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    commentForm.addEventListener('submit', function (e) {
        e.preventDefault();
        console.log('submit button clicked')

        const formData = new FormData(this);

        // Add the song_id to the form data
        const songId = this.getAttribute('data-song-id'); /* logic to get the song_id */
        console.log('songID', songId);
        formData.append('song_id', songId);

        fetch('/comment/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Append the new comment to the existing list
                const commentsList = document.querySelector('.comments-list div');
                console.log(commentsList)
                const p = document.createElement('p');
                p.textContent = `${data.comment.user} - ${data.comment.text}`;
                commentsList.appendChild(p);

                // Clear the input field
                this.querySelector('.comment_input').value = '';
            } else {
                console.log(`Failed to post comment: ${data.message}`);
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



// document.addEventListener('DOMContentLoaded', function () {
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     const likeButtons = document.querySelectorAll('.like-btn');
//
//     // Establish WebSocket connection
//     const socketProtocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
//     const socket = new WebSocket(socketProtocol + window.location.host + '/ws/songs/');
//
//     // WebSocket connection opened event
//     socket.addEventListener('open', (event) => {
//         console.log('WebSocket connection opened:', event);
//
//         // Like button click event
//         likeButtons.forEach(button => {
//             button.addEventListener('click', function () {
//                 console.log('Like button clicked');
//                 const songId = this.getAttribute('data-song-id');
//                 const action = this.classList.contains('liked') ? 'unlike' : 'like';
//
//                 fetch('/like/', {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/x-www-form-urlencoded',
//                         'X-CSRFToken': csrftoken
//                     },
//                     body: `song_id=${encodeURIComponent(songId)}&action=${action}`
//                 })
//                 .then(response => response.json())
//                 .then(data => {
//                     console.log('Response data:', data);
//
//                     if (data.status === 'error') {
//                         console.error('Error:', data.message);
//                     } else {
//                         // Toggle the visual state of the like button
//                         const isLiked = data.is_liked;
//                         if (isLiked) {
//                             this.classList.add('liked');
//                             console.log('User liked the song');
//                         } else {
//                             this.classList.remove('liked');
//                             console.log('User unliked the song');
//                         }
//
//                         // Update the likes count on the client side
//                         const likeCount = this.parentElement.querySelector('.like-count');
//                         if (likeCount) {
//                             likeCount.textContent = data.likes;
//                             console.log('Updated like count:', data.likes);
//                         }
//
//                         // Send WebSocket message for real-time update
//                         socket.send(JSON.stringify({
//                             action: action,
//                             song_id: songId,
//                             likes_count: data.likes
//                         }));
//                     }
//                 })
//                 .catch(error => {
//                     console.error('Error:', error.message);
//                     console.log('Error response:', error.response);
//                 });
//             });
//         });
//     });
//
//     // WebSocket message received event
//     socket.addEventListener('message', (event) => {
//         const data = JSON.parse(event.data);
//         console.log('WebSocket message received:', data);
//
//         // Update like count on the client side
//         const likeButton = document.querySelector(`.like-btn[data-song-id="${data.song_id}"]`);
//         if (likeButton) {
//             const likeCount = likeButton.parentElement.querySelector('.like-count');
//             if (likeCount) {
//                 likeCount.textContent = data.likes_count;
//                 console.log('Updated like count from WebSocket:', data.likes_count);
//             }
//         }
//     });
// });
