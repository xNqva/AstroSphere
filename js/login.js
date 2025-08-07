function toggleForm() {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    if (loginForm.classList.contains('hidden')) {
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
    } else {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
    }
}

document.getElementById("registerForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = {
        first_name: $(".first_name").val(),
        last_name: $(".last_name").val(),
        username: $(".username").val(),
        email: $(".email").val(),
        password: $(".password").val(),
        confirm_password: $(".confirm_pass").val() // Include confirm password
    };

    const response = await fetch("http://127.0.0.1:5000/login", { // Use the same endpoint
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
    });

    const result = await response.json();
    alert(result.message || result.error); // Show success or error message

    if (response.ok) {
        toggleForm(); // Switch to login form after successful registration
    }
});

document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = {
        username: $("#login_username").val(), 
        password: $("#login_password").val() 
    };

    const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
    });

    const result = await response.json();
    alert(result.message || result.error); // Show success or error message

    if (response.ok) {
        window.location.href = "http://127.0.0.1:5000/dashboard"; // Redirect to dashboard or main page
    }
});