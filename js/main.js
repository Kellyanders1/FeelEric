document.addEventListener('DOMContentLoaded', () => {

    /* Custom Cursor Logic */
    const cursor = document.querySelector('.custom-cursor');
    const hoverTargets = document.querySelectorAll('.hover-target, a, button');

    if (cursor) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.top = e.clientY + 'px';
            cursor.style.left = e.clientX + 'px';
        });

        hoverTargets.forEach(target => {
            target.addEventListener('mouseenter', () => {
                cursor.classList.add('hovered');
            });
            target.addEventListener('mouseleave', () => {
                cursor.classList.remove('hovered');
            });
        });
    }

    /* Menu Toggle Logic */
    const menuBtn = document.getElementById('menu-btn');
    const menuClose = document.getElementById('menu-close');
    const menuOverlay = document.getElementById('menu-overlay');

    if (menuBtn && menuClose && menuOverlay) {
        menuBtn.addEventListener('click', () => {
            menuOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        });

        menuClose.addEventListener('click', () => {
            menuOverlay.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    /* Update Footer Year */
    const yearElem = document.getElementById('year');
    if (yearElem) {
        yearElem.textContent = new Date().getFullYear();
    }

    /* Reveal on Scroll */
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const introText = document.querySelector('.intro-text');
    if (introText) {
        introText.style.opacity = 0;
        introText.style.transform = 'translateY(30px)';
        introText.style.transition = 'all 1s ease';
        observer.observe(introText);
    }

    /*Video Default Setup (SAFE)*/
    const videoTitle = document.getElementById("videoTitle");
    if (videoTitle) {
        videoTitle.innerText = "Alterfin: supporting over 1,400 coffee farmers at Nyamurinda, Rwanda";
    }

});


/*VIDEO FUNCTIONS (GLOBAL - VERY IMPORTANT)*/

function changeVideo(videoId, title) {
    const frame = document.getElementById("videoFrame");
    if (!frame) return;

    frame.src = "https://www.youtube.com/embed/" + videoId;
}