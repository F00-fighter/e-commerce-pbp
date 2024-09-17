document.addEventListener('DOMContentLoaded', function () {
    const scrollContent = document.querySelector('.scroll-content');
    const scrollButtons = document.querySelectorAll('.scroll-button');
    const featureItems = document.querySelectorAll('.feature-item');
    let currentIndex = 0;

    function updateScroll() {
        const offset = -currentIndex * 100;
        scrollContent.style.transform = `translateX(${offset}%)`;
    }

    scrollButtons.forEach(button => {
        button.addEventListener('click', function () {
            if (button.classList.contains('left')) {
                currentIndex = (currentIndex > 0) ? currentIndex - 1 : featureItems.length - 1;
            } else {
                currentIndex = (currentIndex < featureItems.length - 1) ? currentIndex + 1 : 0;
            }
            updateScroll();
        });
    });
});