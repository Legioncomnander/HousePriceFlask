// Variable Declaration
const loginBtn = document.querySelector("#login");
const registerBtn = document.querySelector("#register");
const loginForm = document.querySelector(".login-form");
const registerForm = document.querySelector(".register-form");
const registerHomeBtn = document.querySelector("#registerHomeBtn"); // New

// Login button function
function showLoginForm() {
    loginBtn.style.backgroundColor = "#21264D";
    registerBtn.style.backgroundColor = "rgba(255,255,255,0.2)";

    loginForm.style.left = "50%";
    registerForm.style.left = "-50%";

    loginForm.style.opacity = 1;
    registerForm.style.opacity = 0;
}

loginBtn.addEventListener('click', showLoginForm);

// Register button function
registerBtn.addEventListener('click', () => {
    loginBtn.style.backgroundColor = "rgba(255,255,255,0.2)";
    registerBtn.style.backgroundColor = "#21264D"; 

    loginForm.style.left = "150%";
    registerForm.style.left = "50%";

    loginForm.style.opacity = 0;
    registerForm.style.opacity = 1;
})

// Function to show register form and prediction
function showPrediction() {
    loginForm.style.left = "-150%";
    registerForm.style.left = "50%";
    loginForm.style.opacity = 0;
    registerForm.style.opacity = 1;
}

// Check if the prediction exists and call showPrediction if it does
window.onload = () => {
    const prediction = "{{ prediction }}";
    if (prediction) {
        showPrediction();
    }
}

// Register Home button function
registerHomeBtn.addEventListener('click', showLoginForm); // New
