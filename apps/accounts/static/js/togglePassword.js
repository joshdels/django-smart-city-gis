const password = document.getElementById("password");
const toggle = document.getElementById("togglePassword");
const icon = document.getElementById("iconPassword");

const error = document.getElementById("loginError");

toggle.addEventListener("click", () => {
  if (password.type === "password") {
    password.type = "text";
    icon.src = icon.dataset.hide;
  } else {
    password.type = "password";
    icon.src = icon.dataset.show;
  }
});


if (error) {
    setTimeout(() => {
        error.style.display = "none";
    }, 8000);
}
