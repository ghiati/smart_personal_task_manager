document.addEventListener('DOMContentLoaded', () => {
    // Example: Add form validation or custom interactions
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const taskForm = document.getElementById('task-form');

    // Login Form Validation
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            const username = loginForm.querySelector('input[name="username"]').value.trim();
            const password = loginForm.querySelector('input[name="password"]').value.trim();

            if (!username || !password) {
                event.preventDefault();
                alert('Please enter both username and password.');
            } else {
                console.log('Login form submitted');
            }
        });
    }

    // Register Form Validation
    if (registerForm) {
        registerForm.addEventListener('submit', (event) => {
            const username = registerForm.querySelector('input[name="username"]').value.trim();
            const password = registerForm.querySelector('input[name="password"]').value.trim();
            const confirmPassword = registerForm.querySelector('input[name="confirm_password"]').value.trim();

            if (!username || !password || !confirmPassword) {
                event.preventDefault();
                alert('Please fill out all fields.');
            } else if (password !== confirmPassword) {
                event.preventDefault();
                alert('Passwords do not match.');
            } else {
                console.log('Register form submitted');
            }
        });
    }

    // Task Form Validation
    if (taskForm) {
        taskForm.addEventListener('submit', (event) => {
            const taskInput = taskForm.querySelector('input[name="task"]').value.trim();

            if (!taskInput) {
                event.preventDefault();
                alert('Please enter a task.');
            } else {
                console.log('Task form submitted');
            }
        });
    }
});
