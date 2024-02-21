document.addEventListener("DOMContentLoaded", function() {
    const recentPosts = document.getElementById('recent-posts');

    recentPosts.addEventListener('click', function() {
        fetch('/static/exercises/try.json')
        .then(response => response.json())
        .then(posts => {
            const postsContainer = document.getElementById('posts-container');
            postsContainer.innerHTML = ''; // Clear previous content

            posts.forEach(post => {
                const postElement = document.createElement('div');
                postElement.classList.add('post');

                const titleElement = document.createElement('h3');
                titleElement.textContent = post.title;

                const contentElement = document.createElement('p');
                contentElement.textContent = post.content;

                const nameElement = document.createElement('p');
                nameElement.textContent = `Posted by ${post.name}`;

                postElement.appendChild(titleElement);
                postElement.appendChild(contentElement);
                postElement.appendChild(nameElement);

                postsContainer.appendChild(postElement);
            });
        })


        .catch(error => {
            console.error('Error fetching data:', error);
        });

        document.addEventListener("DOMContentLoaded", function() {
            const postButton = document.getElementById('postButton');
            const postContentInput = document.getElementById('postContent');
            const postsContainer = document.getElementById('posts-container');
        
            postButton.addEventListener('click', function() {
                const postContent = postContentInput.value;
                
                // Create a new post element
                const newPost = document.createElement('div');
                newPost.classList.add('post');
                
                const postContentElement = document.createElement('p');
                postContentElement.textContent = postContent;
                
                newPost.appendChild(postContentElement);
                
                // Append the new post to the posts container
                postsContainer.appendChild(newPost);
                
                // Clear the input field after posting
                postContentInput.value = '';
            });
        });
        
    });
});
