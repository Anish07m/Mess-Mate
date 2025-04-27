// Modal Animation (Smooth open/close)
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('exampleModal');
    const modalTrigger = document.getElementById('modalButton');
    const modalClose = document.querySelector('.btn-close');

    if (modal && modalTrigger && modalClose) {
        modalTrigger.addEventListener('click', function () {
            modal.style.display = 'block';
            modal.classList.add('fade-in');
        });

        modalClose.addEventListener('click', function () {
            modal.style.display = 'none';
            modal.classList.remove('fade-in');
        });
    }

    // Live Search (Filters items in a list as you type)
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function (e) {
            const searchQuery = e.target.value.toLowerCase();
            const items = document.querySelectorAll('.search-item');

            items.forEach(item => {
                const itemText = item.textContent.toLowerCase();
                item.style.display = itemText.includes(searchQuery) ? 'block' : 'none';
            });
        });
    }

    // Image Gallery (Click to open image in modal)
    const galleryImages = document.querySelectorAll('.gallery-image');
    const modalImage = document.getElementById('modalImage');
    const imageModal = document.getElementById('imageModal');
    const closeImage = document.querySelector('.close-image');

    if (galleryImages.length && modalImage && imageModal && closeImage) {
        galleryImages.forEach(image => {
            image.addEventListener('click', function () {
                modalImage.src = this.src;
                imageModal.style.display = 'block';
            });
        });

        closeImage.addEventListener('click', function () {
            imageModal.style.display = 'none';
        });
    }

    // Form Validation (Feedback)
    const feedbackForm = document.getElementById('feedbackForm');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function (e) {
            const nameField = document.getElementById('name');
            const messageField = document.getElementById('message');

            if (!nameField.value.trim() || !messageField.value.trim()) {
                e.preventDefault();
                showNotification('Please fill out all fields!');
            }
        });
    }

    // Theme Toggle
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-theme');
        });
    }
});

// Notification System (Global Access)
function showNotification(message) {
    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('hide');
        notification.addEventListener('transitionend', () => notification.remove());
    }, 2500);
}
