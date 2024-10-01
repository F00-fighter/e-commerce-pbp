document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById('hamburger');
    const nav = document.querySelector('.nav-stuff');
    const loginInfo = document.querySelector('.login-info');

    hamburger.addEventListener('click', function() {
        nav.classList.toggle('active');
        loginInfo.classList.toggle('active');
    });
});
