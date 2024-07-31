document.addEventListener('DOMContentLoaded', () => {
    // Example: Add form validation or custom interactions
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            // Add custom validation or interaction
            console.log('Login form submitted');
        });
    }
    
    if (registerForm) {
        registerForm.addEventListener('submit', (event) => {
            // Add custom validation or interaction
            console.log('Register form submitted');
        });
    }
});
