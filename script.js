const burger = document.querySelector(`.burger`);
const navLinks = document.querySelector(`.nav-links`);

burger.addEventListener(`click`,()=>{
    navLinks.classList.toggle(`nav-active`);
})

const heroSlide = document.querySelector('.carousel-slide');
const heroItems = document.querySelectorAll('.hero-item');
const prevHeroBtn = document.querySelector('.hero-carousel .prev');
const nextHeroBtn = document.querySelector('.hero-carousel .next');

let heroCounter = 0;

function showHeroSlide() {
    heroSlide.style.transform = `translateX(${-heroCounter * 100}%)`;
}

nextHeroBtn.addEventListener('click', () => {
    heroCounter = (heroCounter + 1) % heroItems.length;
    showHeroSlide();
});

prevHeroBtn.addEventListener('click', () => {
    heroCounter = (heroCounter - 1 + heroItems.length) % heroItems.length;
    showHeroSlide();
});

// Optional: Auto-play every 5 seconds
setInterval(() => {
    heroCounter = (heroCounter + 1) % heroItems.length;
    showHeroSlide();
}, 5000);

