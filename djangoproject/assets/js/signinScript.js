let openLogin = document.querySelector('.h1','.h1v2');
let loginWrapper = document.querySelector('.login-wrapper');

openLogin.addEventListener('click', function() {
    loginWrapper.classList.toggle('open');
});
