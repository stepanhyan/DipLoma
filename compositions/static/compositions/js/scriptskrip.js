// document.addEventListener('DOMContentLoaded', function () {
//         const commentForms = document.querySelectorAll('.comment-form');
//
//         commentForms.forEach(form => {
//             form.addEventListener('submit', function (e) {
//                 e.preventDefault();
//
//                 const formData = new FormData(this);
//
//                 fetch('/comment/', {
//                     method: 'POST',
//                     body: formData
//                 })
//                     .then(response => response.json())
//                     .then(data => {
//                         if (data.status === 'success') {
//                             // Обновите отображение комментариев на странице, например, добавьте их в соответствующий div
//                             const commentsDiv = form.parentElement.querySelector('.comments');
//                             commentsDiv.textContent = data.comments;
//                         } else {
//                             alert('Failed to post comment.');
//                         }
//                     })
//                     .catch(error => console.error('Error:', error));
//             });
//         });
//     });
//
// // debugger
// document.addEventListener('DOMContentLoaded', function () {
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     const likeButtons = document.querySelectorAll('.like-btn');
//
//     function updateLikeCount(button, likes, songId) {
//         console.log('Updating like count:', likes); // Add this line for debugging
//         const likeCount = button.parentElement.querySelector(`#like-count-${songId}`);
//         console.log('Like count element:', likeCount); // Add this line for debugging
//         if (likeCount) {
//            likeCount.textContent = likes;
//         }
//     }
//
//     likeButtons.forEach(button => {
//         button.addEventListener('click', function () {
//             console.log('Like button clicked');
//             const songId = this.getAttribute('data-song-id');
//
//             fetch('/like/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/x-www-form-urlencoded',
//                     'X-CSRFToken': csrftoken
//                 },
//                 body: `song_id=${encodeURIComponent(songId)}`
//             })
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error('Failed to like the song.');
//                 }
//                 return response.json();
//             })
//             .then(data => {
//                 console.log('Response data:', data);
//
//                 if (data.status === 'error') {
//                     console.error('Error:', data.message);
//                 } else {
//                     // Update the likes count on the client side
//                     updateLikeCount(this, data.likes, songId);
//
//                     // Toggle the visual state of the like button
//                     const isLiked = data.is_liked;
//                     if (isLiked) {
//                         this.classList.add('liked');
//                         console.log('User liked the song');
//                     } else {
//                         this.classList.remove('liked');
//                         console.log('User unliked the song');
//                     }
//                 }
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     });
// });
//
