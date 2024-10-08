// Add event listeners for delete buttons
function addDeleteThreadEventListeners() {
    document.querySelectorAll('.delete-thread-btn').forEach(button => {
        button.addEventListener('click', function () {
            const threadId = this.dataset.threadId;

            fetch(`/community/thread/${threadId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Remove the thread from the DOM
                    document.getElementById(`thread-${threadId}`).remove();
                } else {
                    alert(data.message);
                }
            })
            .catch(err => {
                console.error('Error:', err);
                alert('An error occurred while deleting the thread.');
            });
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('thread-modal');
    const openBtn = document.getElementById('open-modal-btn');
    const closeBtn = document.querySelector('.close-btn');

    // Open the modal when the button is clicked
    openBtn.addEventListener('click', function() {
        console.log('Open button clicked'); 
        modal.style.display = 'block';
    });

    // Close the modal when the close button is clicked
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close the modal when clicking outside the modal content
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Prevent form submission to reload the page
    const createThreadForm = document.querySelector('#create-thread-form');
    if (createThreadForm) {
        createThreadForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Append the new thread to the thread list
                    const threadList = document.querySelector('.thread-list');
                    threadList.innerHTML += `
                        <li class="thread-item" id="thread-${data.thread.id}">
                            <h3>${data.thread.title}</h3>
                            <p>${data.thread.content}</p>
                            <p>Posted by: ${data.thread.user} on ${data.thread.created_at}</p>
                            <button class="delete-thread-btn" data-thread-id="${data.thread.id}">Delete</button>
                        </li>`;
                    
                    // Re-apply delete event listeners
                    addDeleteThreadEventListeners();
                    
                    // Clear the form and close the modal
                    this.reset();
                    modal.style.display = "none";
                } else {
                    alert(data.message);
                }
            })
            .catch(err => {
                console.error('Error:', err);
                alert('An error occurred while creating the thread.');
            });
        });
    }

    // Initialize delete event listeners for existing threads
    addDeleteThreadEventListeners();
});
