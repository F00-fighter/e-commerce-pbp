document.addEventListener('DOMContentLoaded', function () {
    const scrollContent = document.querySelector('.scroll-content');
    const scrollButtons = document.querySelectorAll('.scroll-button');
    const featureItems = document.querySelectorAll('.feature-item');
    let currentIndex = 0;

    function updateScroll() {
        const offset = -currentIndex * 100;
        scrollContent.style.transform = `translateX(${offset}%)`;
    }

    // Add auto-scrolling functionality
    function autoScroll() {
        currentIndex = (currentIndex < featureItems.length - 1) ? currentIndex + 1 : 0;
        updateScroll();
    }

    // Set interval for auto-scrolling every 5 seconds
    let autoScrollInterval = setInterval(autoScroll, 5000);

    // Manual scrolling overrides auto-scrolling
    scrollButtons.forEach(button => {
        button.addEventListener('click', function () {
            clearInterval(autoScrollInterval); // Stop auto-scroll on manual scroll
            if (button.classList.contains('left')) {
                currentIndex = (currentIndex > 0) ? currentIndex - 1 : featureItems.length - 1;
            } else {
                currentIndex = (currentIndex < featureItems.length - 1) ? currentIndex + 1 : 0;
            }
            updateScroll();
            // Restart auto-scrolling after 5 seconds of inactivity
            autoScrollInterval = setInterval(autoScroll, 5000);
        });
    });
});
