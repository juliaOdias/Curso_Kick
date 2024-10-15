const navbar_btt = document.querySelector(".navbar_button");
const navbar_links = document.querySelector(".navbar_links");
const navbar = document.querySelector(".navbar");

function toggle_menu(event) {
    if (event.type === 'touchstart') event.preventDefault();

    navbar_links.classList.toggle('active');
    navbar.classList.toggle('active');
}

navbar_btt.addEventListener('click', toggle_menu);
navbar_btt.addEventListener('touchstart', toggle_menu);

function navigateTo(page) {
    console.log("Navigating to", page);
    window.location.href = page;
}
